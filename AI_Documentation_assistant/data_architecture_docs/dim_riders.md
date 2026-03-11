---
table_name: dim_riders
domain: marketplace
table_type: dimension
grain: one_record_per_rider

table_description: >
  Dimension table containing rider profile information.
  The grain of the table is one record per rider.

fields:
  - field_name: rider_id
    data_type: STRING
    key_type: PRIMARY_KEY
    description: Unique identifier for each rider on the platform.

  - field_name: signup_date
    data_type: DATE
    key_type: NONE
    description: Date when the rider signed up on the platform.

  - field_name: home_city
    data_type: STRING
    key_type: NONE
    description: Primary city where the rider is located.

  - field_name: rider_rating
    data_type: FLOAT
    key_type: NONE
    description: Average rating given to the rider by drivers.

  - field_name: rider_status
    data_type: STRING
    key_type: NONE
    description: Current status of rider account (Active, Suspended, Inactive).
---

# Table: dim_riders

## Description
This dimension table stores **rider profile attributes**.

**Grain:** One record per rider.

The table provides additional context for trip-level analyses.

---

## Field Definitions

| Field Name | Data Type | Key Type | Description |
|------------|-----------|----------|-------------|
| rider_id | STRING | Primary Key | Unique rider identifier |
| signup_date | DATE | None | Date rider joined platform |
| home_city | STRING | None | Primary city of rider |
| rider_rating | FLOAT | None | Average driver rating for rider |
| rider_status | STRING | None | Account status of rider |

---

## Analytical Use Cases

- Rider cohort analysis
- Rider retention
- Rider segmentation by city
