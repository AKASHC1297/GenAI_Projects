---
table_name: dim_drivers
domain: marketplace
table_type: dimension
grain: one_record_per_driver

table_description: >
  Dimension table containing profile and metadata information about drivers
  registered on the ride-hailing platform. The grain of the table is one
  record per driver.

fields:
  - field_name: driver_id
    data_type: STRING
    key_type: PRIMARY_KEY
    description: Unique identifier for each driver on the platform.

  - field_name: signup_date
    data_type: DATE
    key_type: NONE
    description: Date when the driver registered on the platform.

  - field_name: city_id
    data_type: STRING
    key_type: FOREIGN_KEY
    description: Identifier for the city where the driver primarily operates.

  - field_name: vehicle_type
    data_type: STRING
    key_type: NONE
    description: Type of vehicle used by the driver (Sedan, Hatchback, Auto, etc).

  - field_name: driver_rating
    data_type: FLOAT
    key_type: NONE
    description: Average rating given to the driver by riders.

  - field_name: driver_status
    data_type: STRING
    key_type: NONE
    description: Current status of the driver (Active, Suspended, Inactive).
---

# Table: dim_drivers

## Description
This dimension table stores **driver profile information**.

**Grain:** One record per driver.

It is used to enrich trip-level data with driver attributes such as:

- Driver location
- Vehicle category
- Driver ratings

---

## Field Definitions

| Field Name | Data Type | Key Type | Description |
|------------|-----------|----------|-------------|
| driver_id | STRING | Primary Key | Unique identifier for each driver |
| signup_date | DATE | None | Date when driver joined the platform |
| city_id | STRING | Foreign Key | City where driver primarily operates |
| vehicle_type | STRING | None | Category of vehicle used by driver |
| driver_rating | FLOAT | None | Average rider rating for the driver |
| driver_status | STRING | None | Status of driver (Active / Suspended / Inactive) |

---

## Analytical Use Cases

- Driver supply analysis
- Vehicle type segmentation
- Driver retention analysis
