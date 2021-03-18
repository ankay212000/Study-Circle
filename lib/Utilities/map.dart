import 'dart:async';
import 'package:flutter/material.dart';
import 'package:google_maps_flutter/google_maps_flutter.dart';
import 'package:geolocator/geolocator.dart';

class Map extends StatefulWidget {
  final double longitute;
  final double latitude;

  Map({
    Key key,
    @required this.longitute,
    @required this.latitude,
  }) : super(key: key);

  @override
  _MapState createState() => _MapState();
}

class _MapState extends State<Map> {
  Completer<GoogleMapController> _controller = Completer();
  List<Marker> _markers = <Marker>[];
  final Geolocator geolocator = Geolocator()..forceAndroidLocationManager;
  String _currentLocality,_currentCodeAndCountry;

  _getAddressFromLatLng() async {
    try {
      List<Placemark> p = await geolocator.placemarkFromCoordinates(
          widget.latitude, widget.longitute);

      Placemark place = p[0];

      setState(() {
        _currentLocality =
            "${place.locality}" ;
        _currentCodeAndCountry="${place.postalCode}, ${place.country}";
      });
    } catch (e) {
      print(e);
    }
    addMarker();
  }

  void addMarker() {
    _markers.add(
      Marker(
        markerId: MarkerId('1'),
        position: LatLng(widget.latitude, widget.longitute),
        infoWindow: InfoWindow(title: _currentLocality, snippet: _currentCodeAndCountry),
      ),
    );
  }

  void initState() {
    super.initState();
    _getAddressFromLatLng();
  }

  @override
  Widget build(BuildContext context) {
    return new Scaffold(
      appBar: AppBar(
        // iconTheme: IconThemeData( color: Colors. black),
        title: Text("Location on map",style:TextStyle(color: Colors.white),),
        backgroundColor: Color(0xFF7A9BEE),
      ),
      body: GoogleMap(
        mapType: MapType.normal,
        markers: Set<Marker>.of(_markers),
        initialCameraPosition: CameraPosition(
            bearing: 192.8334901395799,
            target: LatLng(widget.latitude, widget.longitute),
            zoom: 15),
        onMapCreated: (GoogleMapController controller) {
          _controller.complete(controller);
        },
      ),
    );
  }
}