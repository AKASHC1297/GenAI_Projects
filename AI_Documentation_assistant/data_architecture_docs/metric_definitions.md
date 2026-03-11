---
company: SwiftRide
document_type: metric_definitions
domain: ride_hailing_marketplace

metrics:

  - metric_name: total_trips
    description: Total number of completed trips on the platform.
    formula: COUNT(trips where trip_status = 'Completed')
    sql_example: |
      SELECT COUNT(*)
      FROM fct_trip
      WHERE trip_status = 'Completed'
    source_tables:
      - fct_trip
    business_impact: >
      Represents the core demand and revenue generating activity of the platform.

  - metric_name: total_sessions
    description: Total number of application sessions initiated by users.
    formula: COUNT(all sessions)
    sql_example: |
      SELECT COUNT(*)
      FROM fact_app_sessions
    source_tables:
      - fact_app_sessions
    business_impact: >
      Measures user engagement and platform usage.

  - metric_name: total_supply_hours
    description: Total time drivers were online and available on the platform.
    formula: SUM(online_minutes) / 60
    sql_example: |
      SELECT SUM(online_minutes) / 60
      FROM fct_driver_supply_hours
    source_tables:
      - fct_driver_supply_hours
    business_impact: >
      Represents the total supply available in the marketplace.

  - metric_name: trip_completion_rate
    description: Percentage of trip requests that were successfully completed.
    formula: Completed Trips / Total Trip Requests
    sql_example: |
      SELECT
        COUNT(CASE WHEN trip_status = 'Completed' THEN 1 END) * 1.0 /
        COUNT(*) AS trip_completion_rate
      FROM fct_trip
    source_tables:
      - fct_trip
    business_impact: >
      Measures marketplace efficiency and how well supply meets rider demand.

  - metric_name: trip_cancellation_rate
    description: Percentage of trips cancelled by riders or drivers.
    formula: Cancelled Trips / Total Trip Requests
    sql_example: |
      SELECT
        COUNT(CASE WHEN trip_status IN ('Driver Cancelled','Rider Cancelled') THEN 1 END) * 1.0 /
        COUNT(*) AS trip_cancellation_rate
      FROM fct_trip
    source_tables:
      - fct_trip
    business_impact: >
      High cancellation rates indicate marketplace inefficiencies or rider dissatisfaction.

  - metric_name: driver_utilisation
    description: Percentage of time drivers spend completing trips relative to time online.
    formula: Busy Minutes / Online Minutes
    sql_example: |
      SELECT
        SUM(busy_minutes) * 1.0 / SUM(online_minutes)
      FROM fct_driver_supply_hours
    source_tables:
      - fct_driver_supply_hours
    business_impact: >
      Measures how efficiently driver supply is being used.

  - metric_name: average_trip_distance
    description: Average distance travelled per completed trip.
    formula: AVG(trip_distance)
    sql_example: |
      SELECT AVG(trip_distance)
      FROM fct_trip
      WHERE trip_status = 'Completed'
    source_tables:
      - fct_trip
    business_impact: >
      Helps understand rider travel behavior and demand patterns.

  - metric_name: active_drivers
    description: Number of drivers completing at least one trip in a given period.
    formula: COUNT(DISTINCT driver_id)
    sql_example: |
      SELECT COUNT(DISTINCT driver_id)
      FROM fct_trip
      WHERE trip_status = 'Completed'
    source_tables:
      - fct_trip
      - dim_drivers
    business_impact: >
      Indicates active driver participation in the marketplace.

  - metric_name: active_riders
    description: Number of riders requesting at least one trip in a given period.
    formula: COUNT(DISTINCT rider_id)
    sql_example: |
      SELECT COUNT(DISTINCT rider_id)
      FROM fct_trip
    source_tables:
      - fct_trip
      - dim_riders
    business_impact: >
      Represents active demand on the platform.

  - metric_name: average_session_duration
    description: Average duration of app sessions.
    formula: AVG(session_duration_seconds)
    sql_example: |
      SELECT AVG(session_duration_seconds)
      FROM fact_app_sessions
    source_tables:
      - fact_app_sessions
    business_impact: >
      Measures user engagement with the platform.
