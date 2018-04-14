var fourSquareClientId = 'SFYUEK4DZVRCTYTHRRHLDRF3GIRH0ZKGCMBBTGSFDRQKNCQK';
var fourSquareClientSecret = 'TKYEKAQYT1VEKPGP5U2BWHHQOUMNZIJEUXQBBRKDVZAKMPQW';

// initialize a map function

var map;

function initMap() {
    map = new google.maps.Map(document.getElementById('map'), {
        center: {
            lat: 30.060077,
            lng: 31.357876
        },
        styles: mapStyles,
        zoom: 12
    });
}

// prepare places with info function
var PreparePlace = function(place) {
    var self = this;

    // Create Place attributes
    this.name = place.name;
    this.lat = place.lat;
    this.long = place.long;
    this.street = 'N/A';
    this.city = 'N/A';
    this.phone = 'N/A';
    this.visible = ko.observable(true);
    this.infoWindow = new google.maps.InfoWindow({
        content: ''
    });
    // Create FourSquare Url
    var url = 'https://api.foursquare.com/v2/venues/search?ll=' +
        this.lat + ',' + this.long +
        '&query=' + this.name +
        '&client_secret=' + fourSquareClientSecret +
        '&client_id=' + fourSquareClientId +
        '&v=' + '20170801' +
        '&limit=1'

    // using Ajax get details for FourSquare
    $.getJSON(url).done(function(data) {
            var first_place = data.response.venues[0];
            if (first_place) {
                self.street = first_place
                    .location.formattedAddress[0] || self.street;
                self.city = first_place
                    .location.formattedAddress[1] || self.city;
                self.phone = first_place.contact.formattedPhone || self.phone;
            }
        })
        .fail(function() {
            alert(`FourSquare Error!! with ${self.name}`);
        });

    // create a marker
    self.marker = new google.maps.Marker({
        position: new google.maps.LatLng(self.lat, self.long),
        title: self.title,
        animation: google.maps.Animation.DROP
    });

    // show map pins
    ko.computed(function() {
        this.marker.setMap(this.visible() ? map : null);
    }, this);

    this.marker.addListener('click', function() {
        var content = '<div class="container">' +
            '<h3>' + self.name + '</h3>' +
            '<p> Street: ' + self.street + '</p>' +
            '<p> City: ' + self.city + '</p>' +
            '<p> Phone: ' + self.phone + '</p>' +
            '</div>';
        self.infoWindow.setContent(content);
        self.infoWindow.open(map, this);
        self.marker.setAnimation(google.maps.Animation.DROP);
    });
}


PreparePlace.prototype.show = function() {
    google.maps.event.trigger(this.marker, 'click');
};

function AppViewModel() {
    initMap();

    var self = this;
    this.keyword = ko.observable('');
    this.filtered_list = [];

    locations.forEach(function(place, index) {
        locations[index] = new PreparePlace(place)
    });

    this.filtered_list = ko.computed(function() {
        return ko.utils.arrayFilter(locations, function(location) {
            var is_visible = location.name.toLowerCase()
                .includes(self.keyword().toLowerCase());
            location.visible(is_visible);
            return is_visible;
        });
    });
}

function main() {
    ko.applyBindings(new AppViewModel());
}

function GoogleMapsErrorHandler() {
    alert('Faild to load google maps, it may be ur internet connection');
}
