# Fleet Management System

A simple Fleet Management System built using the Frappe Framework as a Week 1 POC.

## Features

- Vehicle management
- Driver management
- Trip management
- Vehicle maintenance records
- Role-based permissions
- Python backend logic
- Client Script with frappe.call
- REST API

## DocTypes

### Vehicle
- Vehicle Number
- Vehicle Type
- Model
- Status

### Driver
- Driver Name
- License Number
- Phone

### Trip
- Vehicle
- Driver
- Source
- Destination
- Trip Date

### Maintenance
- Vehicle
- Service Date
- Cost
- Description

## Backend

Vehicle validation and business logic are handled using Python.

- validate() checks the vehicle number.
- before_save() checks the vehicle model when the vehicle is under maintenance.
- on_submit() shows a submission message.

Frappe ORM is used for database operations such as get_doc(), get_list() and new_doc().

## Client Script

A Check Vehicle button is added to the Trip form.

It calls the Python method:

fleet_management.api.check_vehicle

and displays the current vehicle status.

## REST API

Get Vehicles:

curl -X GET "http://fleet.localhost:8000/api/resource/Vehicle" -H "Authorization: token API_KEY:API_SECRET"

Create Vehicle:

curl -X POST "http://fleet.localhost:8000/api/resource/Vehicle" -H "Authorization: token API_KEY:API_SECRET" -H "Content-Type: application/json" -d '{"vehicle_number":"DL01AB1234","vehicle_type":"Sedan","model":"Honda City","status":"Available"}'

Replace API_KEY and API_SECRET with your own credentials.

Do not add real API credentials to the repository.

## Permissions

A Fleet Manager role was created with Read, Write, Create and Delete permissions for Vehicle.

## Setup

bench get-app https://github.com/Gautam-G-404/fleet_management.git --branch develop

bench --site your-site install-app fleet_management

bench start

## Tech Stack

- Frappe Framework
- Python
- JavaScript
- MariaDB
- Redis

### demo

### Vehicle Management
<img width="1917" height="961" alt="image" src="https://github.com/user-attachments/assets/01cd50bf-29ed-4f93-ab83-d29aac86ebb4" />

### Trip Management
<img width="1917" height="963" alt="Screenshot 2026-09-13 143337" src="https://github.com/user-attachments/assets/9b930869-d7f3-417d-abb8-eae8203ffa3b" />

### REST API
<img width="1387" height="706" alt="image" src="https://github.com/user-attachments/assets/d3e58399-e3a7-41d1-ad28-9fdae895329b" />



## License

MIT
