---
company_name: SwiftRide
document_type: business_logic
domain: ride_hailing_marketplace

overview: >
  SwiftRide is a ride-hailing marketplace platform that connects riders with
  nearby drivers through a mobile application. Riders request trips and
  drivers accept and complete these trips. The platform generates revenue
  through commissions charged on completed rides.

core_entities:
  - riders
  - drivers
  - trips
  - app_sessions
  - driver_supply_hours

primary_fact_tables:
  - fct_trip
  - fact_app_sessions
  - fct_driver_supply_hours

primary_dimension_tables:
  - dim_riders
  - dim_drivers
---

# SwiftRide Business Logic

## Overview

SwiftRide is a **two-sided ride-hailing marketplace** connecting riders who need transportation with drivers who provide transportation services.

The platform operates through a **mobile application**, where:

1. Riders request trips.
2. Drivers nearby receive trip requests.
3. A driver accepts the request.
4. The trip is completed and payment is processed.

SwiftRide generates revenue by taking a **commission from completed trips**.

---

## Core Entities

### Riders

Riders are customers who request trips through the SwiftRide mobile application.

Rider data is stored in the table:

