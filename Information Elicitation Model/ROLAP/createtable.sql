-- DIMENSIONS
DROP TABLE IF EXISTS datee;
DROP TABLE IF EXISTS UserDetails;
CREATE TABLE datee (datee timestamp);
CREATE TABLE UserDetails ( userid INT NOT NULL UNIQUE, username VARCHAR(100), userage INT, usergender VARCHAR(100));

-- FACTS
DROP TABLE IF EXISTS Accessibility;
DROP TABLE IF EXISTS DiningFacilities;
DROP TABLE IF EXISTS HotelBrandValue;
DROP TABLE IF EXISTS HotelPolicies;
DROP TABLE IF EXISTS HotelFacilities;
DROP TABLE IF EXISTS UserSatifiability;
DROP TABLE IF EXISTS Preferences;
DROP TABLE IF EXISTS RoomFacilities;
CREATE TABLE Accessibility (userid INT NOT NULL UNIQUE, datee timestamp, locationn VARCHAR(100), occupancy BOOLEAN, weatherconditions VARCHAR(100));
CREATE TABLE DiningFacilities (userid INT NOT NULL UNIQUE, datee timestamp, bar BOOLEAN, lunch BOOLEAN, breakfast BOOLEAN, dinner BOOLEAN);
CREATE TABLE HotelBrandValue (userid INT NOT NULL UNIQUE, datee timestamp, starrating INT, qualityofservice INT, reviewsrating FLOAT);
CREATE TABLE HotelPolicies (userid INT NOT NULL UNIQUE, datee timestamp, cancellationcharges FLOAT, healthcareoptions BOOLEAN, petsallowed BOOLEAN, checkinout VARCHAR(100), medicalcharges FLOAT);
CREATE TABLE HotelFacilities(userid INT NOT NULL UNIQUE, datee timestamp, parking BOOLEAN, swimmingpool BOOLEAN, breakfastincluded BOOLEAN, diningincluded BOOLEAN, orderin BOOLEAN);
CREATE TABLE UserSatisfiability (userid INT NOT NULL UNIQUE, datee timestamp, userrating FLOAT);
CREATE TABLE Preferences (userid INT NOT NULL UNIQUE, datee timestamp, diningoptions INT, periodofstay INT, discount FLOAT, transportcost FLOAT, leisureactivities VARCHAR(100), modeofpayment VARCHAR(100), reservationcost FLOAT);
CREATE TABLE RoomFacilities (userid INT NOT NULL UNIQUE, datee timestamp, singleroom BOOLEAN, deluxesuite BOOLEAN, doubleroom BOOLEAN, attachedbathrooms BOOLEAN, hostelroom BOOLEAN);
