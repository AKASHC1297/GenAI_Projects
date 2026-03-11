---
table_name: fct_driver_supply_hours
domain: marketplace
table_type: fact
grain: one_record_per_driver_per_hour

table_description: >
  Fact table capturing the amount of time drivers are online and available
  on the platform. The grain of the table is one record per driver per hour.

fields:
  - field_name: supply_hour_id
    data_type: STRING
    key_type: PRIMARY_KEY
    description: Unique identifier for each supply hour record.

  - field_name: driver_id
    data_type: STRING
    key_type: FOREIGN_KEY
    description: Identifier for the driver supplying availability.

  - field_name: supply_date
    data_type: DATE
    key_type: NONE
    description: Date corresponding to the supply record.

  - field_name: supply_hour
    data_type: INTEGER
    key_type: NONE
    description: Hour of the day (0-23) representing the supply interval.

  - field_name: online_minutes
    data_type: INTEGER
    key_type: NONE
    description: Total minutes the driver was online during the hour.

  - field_name: busy_minutes
    data_type: INTEGER
    key_type: NONE
    description: Minutes spent completing trips during the hour.

  - field_name: city_id
    data_type: STRING
    key_type: FOREIGN_KEY
    description: City where the driver was supplying during the hour.
---

# Table: fct_driver_supply_hours

## Description
This fact table captures **driver supply availability on the platform**.

**Grain:** One record per driver per hour.

It measures how much time drivers spend online and actively fulfilling trips.

---

## Field Definitions

| Field Name | Data Type | Key Type | Description |
|------------|-----------|----------|-------------|
| supply_hour_id | STRING | Primary Key | Unique identifier for supply record |
| driver_id | STRING | Foreign Key | Driver providing supply |
| supply_date | DATE | None | Date of supply record |
| supply_hour | INTEGER | None | Hour of day (0-23) |
| online_minutes | INTEGER | None | Minutes driver was online |
| busy_minutes | INTEGER | None | Minutes driver spent on trips |
| city_id | STRING | Foreign Key | City where supply occurred |

---

## Analytical Use Cases

- Driver utilization analysis
- Marketplace supply monitoring
- Peak hour supply patterns
