# reachapi

* Used Django, Django Rest Framework, and PostgreSQL to create relevant models
  * RidePostings (Driver posts a ride)
  * RideRequests (Rider requests a ride)
  
* Created serializers for different purposes

  * RidePosting and RideRequest serializers to create their respective models
  * Offer serializers where a
  
    * RidePosting creator (Driver) can offer a rider to take his ride
    * RideRequest creator (Rider) can offer a driver to drive the rider to his destination
  * Accept serializers where a user with a pending offer can accept the offer
  
* Created relevant views and permissions

  * RidePosting and RideRequest ListViews, with relevant filters to filter the data set
  * RidePosting and RideRequest CreateViews, requiring a user to be authenticated to access
  * RidePosting and RideRequest RUDViews, requiring the user to be the owner to update or delete the model
  * RidePosting and RideRequest Offer and Accept Views, allowing users to send offers to other users and accept offers, respectively
