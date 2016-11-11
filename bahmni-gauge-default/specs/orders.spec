Orders Tab related tests
=====================
Created by atmaramn on 09/11/2016

This is an executable specification file which follows markdown syntax.
Every heading in this file denotes a scenario. Every bulleted point denotes a step.
     
Add Radiology Order
----------------

Tags: regression, sanity

* Create a new patient and open visit through API
* On the login page
* Login to the application
* Click on clinical app
* Select existing patient from patient listing page under tab "Active"
* Navigate to consultation
* Go to "Orders" tab
* Select following orders
    |type|orderType|orderName|
    |Radiology|chest|chest, 1 view (x-ray)|
    |Radiology|chest|chest oblique - bilateral (x-ray)|
    |Radiology|chest|chest lateral|
* Unselect following orders
    |type|orderType|orderName|
    |Radiology|chest|chest lateral|
* Enter notes to following "Radiology" orders
    |order|note|
    |chest, 1 view (x-ray)|Notes 1|
* Save the consultation
* Verify order details on orders page
* Verify notes are not editable for "Radiology" orders
* Navigate to patient dashboard
* Verify display control with Caption "Radiology Orders" on dashboard, has the following details
    |details|
    |Chest, 1 view (X-ray)|
    |Chest oblique - Bilateral (X-ray)|
* Open the current visit
* Verify display control with Caption "Pacs Orders Visit Page" on visit page, has the following details
    |details|
    |Chest, 1 view (X-ray)|
    |Chest oblique - Bilateral (X-ray)|
* Open "Orders" tab on visit page
* Verify display control with Caption "Radiology Orders" on visit page, has the following details
    |details|
    |Chest, 1 view (X-ray)|
    |Chest oblique - Bilateral (X-ray)|
* Navigate to dashboard
* Logout the user


Delete Radiology Orders
----------------
Tags: regression, sanity
* Create a new patient and open visit through API
* Add the following orders through API
    |type|category|name|
    |Radiology|chest|chest apical lordotic |
    |Radiology|chest|chest, 1 view (x-ray) |
    |Radiology|chest|chest, 2 views (x-ray)|

* On the login page
* Login to the application
* Click on clinical app
* Select existing patient from patient listing page under tab "Active"

* Navigate to consultation
* Go to "Orders" tab
* Expand "Radiology" section on orders page
* Verify order details on orders page
* Delete the following orders
    |type|category|name|
    |Radiology|chest|chest apical lordotic |
    |Radiology|chest|chest, 1 view (x-ray) |
* Undo deletion of the following orders
    |type|category|name|
    |Radiology|chest|chest apical lordotic |
* Save the consultation
* Expand "Radiology" section on orders page
* Verify order details on orders page
* Navigate to patient dashboard

* Verify display control with Caption "Radiology Orders" on dashboard, has the following details
    |details|
    |CHEST apical lordotic|
    |Chest, 2 views (X-ray)|
* Open the current visit
* Verify display control with Caption "Pacs Orders Visit Page" on visit page, has the following details
    |details|
    |CHEST apical lordotic|
    |Chest, 2 views (X-ray)|
* Open "Orders" tab on visit page
* Verify display control with Caption "Radiology Orders" on visit page, has the following details
    |details|
    |CHEST apical lordotic|
    |Chest, 2 views (X-ray)|


Fulfill Radiology orders
-----------------------

Tags: regression, sanity

* Create a new patient and open visit through API
* Add the following orders through API
    |type|category|name|
    |Radiology|chest|chest apical lordotic|
    |Radiology|chest|chest, 1 view (x-ray)|
    |Radiology|chest|chest, 2 views (x-ray)|
* On the login page
* Login to the application
* Click on orders app
* Search previously created patient with exact identifier on orders search page
* Verify orders on orders fulfilment page
* Fulfill all radiology order details as follow
    |name|note|
    |chest apical lordotic|Note 1|
    |chest, 1 view (x-ray)|Note 2|
    |chest, 2 views (x-ray)|Note 3|
//* Verify order details on orders fulfilment page