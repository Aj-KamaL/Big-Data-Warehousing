import org.apache.spark._
import org.apache.spark.graphx._
import org.apache.spark.rdd.RDD
import java.util.Calendar
import org.apache.spark.sql.{DataFrame, Row, SQLContext}
import org.apache.spark.sql.functions._
import org.apache.spark.{SparkConf, SparkContext}
import org.apache.spark.graphx.{Graph, VertexRDD, Edge => GXEdge}
import org.apache.spark.sql.types.{IntegerType, LongType}
import org.apache.spark.graphx.GraphLoader

val graph = GraphLoader.edgeListFile(sc, "/home/ajkamal/Desktop/zzz/soc-Epinions1.txt")
case class Node(srcId: Long, auth: Double, hub:Double)
val num_count = graph.vertices.count
case class HITS(auth:Double, hub:Double)
def reduction(a:HITS,b:HITS):HITS = HITS(a.auth + b.auth, a.hub + b.hub)
var gx = graph.mapVertices{case (x,y) => Node(x, 1.0/num_count,1.0/num_count)}
println("*******************************************************************************************************")
println("1. Top PageRank Clusttered Nodes")
println(graph.pageRank(0.0001,0.2).vertices.takeOrdered(5)(Ordering[Double].reverse.on(x=>x._2)).mkString("\n"))
println("*******************************************************************************************************")
println()
var ii=1
while (ii<26) 
{
	
	val message: VertexRDD[HITS] = gx.aggregateMessages(itr => {itr.sendToDst(HITS(0.0,itr.srcAttr.hub));
	itr.sendToSrc(HITS(itr.dstAttr.auth,0.0))}, reduction)
	val authsum = message.map(_._2.auth).sum()
	val hubsum = message.map(_._2.hub).sum()
	gx = gx.outerJoinVertices(message) {case (vID, vAttr, optMsg) => {val msg = optMsg.getOrElse(HITS(1.0/num_count, 1.0/num_count))
			Node(vAttr.srcId, if (msg.auth == 0.0) 1.0 else msg.auth , if (msg.hub == 0.0) 1.0 else msg.hub)}
	}
	///////////////////////////////////////////////////
	// here normalize gx.vertices.values(id,auth,hub)  or gx.vertices.(id,Node(id,auth,hub)) on auth
	gx = gx.outerJoinVertices(message) {case (vID, vAttr, optMsg) => {val msg = optMsg.getOrElse(HITS(1.0/num_count, 1.0/num_count))
			Node(vAttr.srcId, if (msg.auth == 0.0) 1.0/num_count else msg.auth/authsum , if (msg.hub == 0.0) 1.0/num_count else msg.hub/hubsum)}
	}
	ii+=1
}



println("*******************************************************************************************************")
println("2.A Top AuthScored(HITS) Clusttered Nodes: AuthScore")
println(gx.vertices.takeOrdered(5)(Ordering[Double].reverse.on(x=>x._2.auth)).mkString("\n"))
println("*******************************************************************************************************")

println()

println("*******************************************************************************************************")
println("2.B Top AuthScored(HITS) Clusttered Nodes: HubScore")
println(gx.vertices.takeOrdered(5)(Ordering[Double].reverse.on(x=>x._2.hub)).mkString("\n"))
println("*******************************************************************************************************")

println("*******************************************************************************************************")
println("3. Top SimRank Clusttered Nodes")
println(graph.personalizedPageRank(18, 0.0001).vertices.takeOrdered(6)(Ordering[Double].reverse.on(x=>x._2)).mkString("\n"))
println("*******************************************************************************************************")
println()

