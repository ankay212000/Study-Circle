import 'package:flutter/material.dart';
import 'package:cloud_firestore/cloud_firestore.dart';
import 'package:cached_network_image/cached_network_image.dart';
import 'package:solution_challenge/Utilities/ShowUp.dart';
import 'package:solution_challenge/Utilities/descriptionText.dart';
import 'package:solution_challenge/Utilities/map.dart';

import 'package:geolocator/geolocator.dart';

class giveHelp extends StatefulWidget {
  @override
  _giveHelpState createState() => _giveHelpState();
}

class _giveHelpState extends State<giveHelp> {
  int delayAmount = 500;
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: SafeArea(
        child: Stack(
          children: [
            Padding(
              padding: EdgeInsets.only(
                  bottom: MediaQuery.of(context).size.height * 0.3),
              child: ShowUp(
                child: Container(
                  decoration: BoxDecoration(
                    borderRadius: BorderRadius.only(
                      bottomLeft: Radius.circular(45.0),
                      bottomRight: Radius.circular(45.0),
                    ),
                    color: Color(0xFF7A9BEE),
                  ),
                  height: MediaQuery.of(context).size.height * 0.2,
                  width: MediaQuery.of(context).size.width,
                  child: ListView(
                    shrinkWrap: true,
                    children: <Widget>[
                      Padding(
                        padding: EdgeInsets.only(
                            top: MediaQuery.of(context).size.height * 0.06,
                            left: MediaQuery.of(context).size.width * 0.06),
                        child: ShowUp(
                          child: Text(
                            "Help Someone",
                            style: TextStyle(
                                fontFamily: 'Montserrat',
                                fontSize:
                                    MediaQuery.of(context).size.width * 0.1,
                                fontWeight: FontWeight.bold,
                                color: Colors.white),
                          ),
                          delay: delayAmount + 200,
                        ),
                      ),
                    ],
                  ),
                ),
              ),
            ),
            Padding(
              padding: EdgeInsets.only(
                top: MediaQuery.of(context).size.height * 0.23,
                left: MediaQuery.of(context).size.width * 0.05,
                right: MediaQuery.of(context).size.width * 0.05,
                bottom: MediaQuery.of(context).size.width * 0.07,
              ),
              child: ShowUp(child: HelpCardStream()),
            ),
          ],
        ),
      ),
      backgroundColor: Colors.white,
    );
  }
}

class HelpCardStream extends StatefulWidget {
  @override
  _HelpCardStreamState createState() => _HelpCardStreamState();
}

class _HelpCardStreamState extends State<HelpCardStream> {
  int delayAmount = 500;

  @override
  Widget build(BuildContext context) {
    return StreamBuilder<QuerySnapshot>(
      stream: FirebaseFirestore.instance.collection("data").snapshots(),
      builder: (context, snapshot) {
        print(snapshot.connectionState);
        if (snapshot.hasData) {
          final List<DocumentSnapshot> documents = snapshot.data.docs;

          return ListView(
              children: documents
                  .map(
                    (doc) => Container(
                      child: HelpCard(
                          url: doc['url'],
                          problem: doc['Problem'],
                          connect_via: doc['Connect via'],
                          latitude: doc['Latitude'],
                          longitude: doc['Longitude']),
                    ),
                  )
                  .toList());
        } else {
          return Center(child: Text("No post found"));
        }
      },
    );
  }
}

class HelpCard extends StatefulWidget {
  final String problem;
  final String connect_via;
  final String url;
  final double longitude;
  final double latitude;

  HelpCard({
    Key key,
    this.problem,
    this.connect_via,
    this.url,
    this.longitude,
    this.latitude,
  }) : super(key: key);
  @override
  _HelpCardState createState() => _HelpCardState();
}

class _HelpCardState extends State<HelpCard> {
  final Geolocator geolocator = Geolocator()..forceAndroidLocationManager;
  String _currentAddress = "";

  _getAddressFromLatLng(double latitude, double longitude) async {
    try {
      List<Placemark> p =
          await geolocator.placemarkFromCoordinates(latitude, longitude);

      Placemark place = p[0];

      setState(() {
        _currentAddress =
            "${place.locality}, ${place.postalCode}, ${place.country}";
      });
    } catch (e) {
      print(e);
    }
  }

  void initState() {
    super.initState();
    _getAddressFromLatLng(widget.latitude, widget.longitude);
  }

  @override
  Widget build(BuildContext context) {
    return _currentAddress == ""
        ? CircularProgressIndicator()
        : Stack(
            children: [
              AnimatedContainer(
                margin: EdgeInsets.only(bottom: 20.0),
                duration: Duration(milliseconds: 500),
                curve: Curves.easeIn,
                decoration: BoxDecoration(
                  borderRadius: BorderRadius.circular(20.0),
                  border: Border.all(
                      color: Colors.blue,
                      width: MediaQuery.of(context).size.width * 0.0009),
                ),
                // height: MediaQuery.of(context).size.height * 0.5,
                width: MediaQuery.of(context).size.width * 0.97,
                child: Column(
                  mainAxisAlignment: MainAxisAlignment.spaceBetween,
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    ShowUp(
                      child: Center(
                        child: Container(
                          child: CachedNetworkImage(
                            imageUrl: widget.url,
                            imageBuilder: (context, imageProvider) => Container(
                              decoration: BoxDecoration(
                                shape: BoxShape.rectangle,
                                borderRadius: BorderRadius.circular(20.0),
                                image: DecorationImage(
                                  image: imageProvider,
                                  fit: BoxFit.fill,
                                ),
                              ),
                            ),
                            placeholder: (context, url) => Center(
                              child: CircularProgressIndicator(
                                semanticsLabel: 'Linear progress indicator',
                              ),
                            ),
                            errorWidget: (context, url, error) =>
                                Icon(Icons.error),
                          ),
                          width: MediaQuery.of(context).size.width * 0.97,
                          height: MediaQuery.of(context).size.height * 0.25,
                          decoration: new BoxDecoration(
                            // color: Colors.blue,
                            shape: BoxShape.rectangle,
                            borderRadius: BorderRadius.circular(80.0),
                          ),
                        ),
                      ),
                    ),
                    Padding(
                      padding: EdgeInsets.only(
                        top: MediaQuery.of(context).size.width * 0.01,
                        left: MediaQuery.of(context).size.width * 0.04,
                        // bottom: MediaQuery.of(context).size.height * 0.04
                      ),
                      child: Container(
                        width: MediaQuery.of(context).size.width * 0.8,
                        child: new DescriptionTextWidget(text: widget.problem),
                      ),
                    ),
                    Padding(
                      padding: EdgeInsets.only(
                        left: MediaQuery.of(context).size.width * 0.04,
                        right: MediaQuery.of(context).size.width * 0.04,
                        bottom: MediaQuery.of(context).size.width * 0.02,
                      ),
                      child: Row(
                        children: [
                          Text(
                            "Connect via (insta/email/phone) : ",
                            style: TextStyle(
                              fontFamily: 'Montserrat',
                              fontSize:
                                  MediaQuery.of(context).size.width * 0.035,
                              fontWeight: FontWeight.w500,
                            ),
                          ),
                          Text(
                            widget.connect_via,
                            style: TextStyle(
                              fontFamily: 'Montserrat',
                              fontSize:
                                  MediaQuery.of(context).size.width * 0.035,
                              color: Colors.grey[700],
                            ),
                          ),
                        ],
                      ),
                    ),
                    Padding(
                      padding: EdgeInsets.only(
                        left: MediaQuery.of(context).size.width * 0.04,
                        right: MediaQuery.of(context).size.width * 0.04,
                        bottom: MediaQuery.of(context).size.width * 0.04,
                      ),
                      child: Row(
                        mainAxisAlignment: MainAxisAlignment.spaceBetween,
                        children: [
                          Expanded(
                            flex: 5,
                            child: Text(
                              _currentAddress != ""
                                  ? _currentAddress
                                  : "No address found",
                              textAlign: TextAlign.left,
                              style: TextStyle(
                                fontFamily: 'Montserrat',
                                fontSize:
                                    MediaQuery.of(context).size.width * 0.033,
                                color: Colors.grey[700],
                              ),
                            ),
                          ),
                          Expanded(
                            flex: 5,
                            child: FlatButton.icon(
                              onPressed: () => {
                                Navigator.push(
                                  context,
                                  MaterialPageRoute(
                                    builder: (context) => Map(
                                      latitude: widget.latitude,
                                      longitute: widget.longitude,
                                    ),
                                  ),
                                )
                              },
                              label: Text(
                                "Show on map",
                                style: TextStyle(
                                    fontFamily: 'Montserrat',
                                    fontSize:
                                        MediaQuery.of(context).size.width *
                                            0.033,
                                    fontWeight: FontWeight.w600,
                                    color: Color(0xFF7A9BEE)),
                              ),
                              icon: Icon(
                                Icons.pin_drop,
                                size: MediaQuery.of(context).size.width * 0.053,
                                color: Color(0xFF7A9BEE),
                              ),
                            ),
                          ),
                        ],
                      ),
                    ),
                  ],
                ),
              ),
            ],
          );
  }
}