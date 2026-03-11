---
table_name: fct_trip

table_description: >
  Fact table containing all trip transactions in the ride-hailing platform.
  Grain: One record per trip request.

fields:
  - field_name: trip_id
    data_type: STRING
    key_type: PRIMARY_KEY
    description: Unique identifier for each trip request.

  - field_name: driver_id
    data_type: STRING
    key_type: FOREIGN_KEY
    description: Identifier for the driver fulfilling the trip. References dim_driver.driver_id.

  - field_name: rider_id
    data_type: STRING
    key_type: FOREIGN_KEY
    description: Identifier for the rider requesting the trip. References dim_rider.rider_id.

  - field_name: trip_distance
    data_type: FLOAT
    key_type: NONE
    description: Total distance travelled during the trip in kilometers.

  - field_name: trip_fare
    data_type: FLOAT
    key_type: NONE
    description: Total fare charged to the rider for the trip.

  - field_name: trip_status
    data_type: STRING
    key_type: NONE
    description: Status of the trip request (Completed, Rider Cancelled, Driver Cancelled).

  - field_name: request_timestamp
    data_type: TIMESTAMP
    key_type: NONE
    description: Timestamp when the rider requested the trip.

  - field_name: completion_timestamp
    data_type: TIMESTAMP
    key_type: NONE
    description: Timestamp when the trip was completed.
---

# Table: fct_trip

## Description
This is the primary transactional fact table for the ride-hailing marketplace.

**Grain:** One record per trip request.

The table captures both completed and cancelled trips and is used for core marketplace analytics including:

- Trip volume analysis
- Revenue analysis
- Driver utilization
- Rider demand patterns

---

## Field Definitions

| Field Name | Data Type | Key Type | Description |
|------------|-----------|----------|-------------|
| trip_id | STRING | Primary Key | Unique identifier for each trip request |
| driver_id | STRING | Foreign Key | References driver fulfilling the trip |
| rider_id | STRING | Foreign Key | References rider requesting the trip |
| trip_distance | FLOAT | None | Distance travelled during trip in kilometers |
| trip_fare | FLOAT | None | Total fare charged to the rider |
| trip_status | STRING | None | Status of trip (Completed / Cancelled) |
| request_timestamp | TIMESTAMP | None | Time when trip was requested |
| completion_timestamp | TIMESTAMP | None | Time when trip was completed |

---

## Analytical Use Cases

This table is commonly used for:

- Trip completion rate calculation
- Driver supply analysis
- Revenue reporting
- Demand forecasting

---

## Example Analytical Query

```sql
SELECT
    DATE(request_timestamp) AS trip_date,
    COUNT(*) AS total_trips
FROM fct_trip
WHERE trip_status = 'Completed'
GROUP BY 1
