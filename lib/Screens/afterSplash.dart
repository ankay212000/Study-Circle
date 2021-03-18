import 'package:flutter/material.dart';
import 'subHome.dart';
import '../Utilities/ShowUp.dart';
import 'package:solution_challenge/Problem_Submission/registerProblem.dart';
import 'package:solution_challenge/Problem_Submission/Provide_Help.dart';
import 'package:geolocator/geolocator.dart';

class pageHome extends StatefulWidget {
  @override
  _pageHomeState createState() => _pageHomeState();
}

class _pageHomeState extends State<pageHome> {
  var delay=100;
  String selected;
  final Geolocator geolocator = Geolocator()..forceAndroidLocationManager;
  Position _currentPosition;

  void initState() {
    super.initState();
    _getCurrentLocation();
  }
  void changeName(String txt){
    setState(() {
      selected = txt;
    });
  }
  @override
  Widget build(BuildContext context) {
    var height=MediaQuery.of(context).size.height;
    var width=MediaQuery.of(context).size.width;
    return Scaffold(
      backgroundColor: Colors.green,
      body: Center(
        child: Container(
          height: height*0.9,
          width: width*0.95,
          decoration: BoxDecoration(
            borderRadius: BorderRadius.only(
            topLeft: Radius.circular(45.0),
            topRight: Radius.circular(45.0),
            bottomLeft: Radius.circular(45.0),
            bottomRight: Radius.circular(45.0),
          ),
        color: Colors.white,
      ),
      child: Stack(children: [
        Container(
                  child: Column(
                        children:[
                          ShowUp(
                      child: Stack(children:[
                        ShowUp(child: Padding(
                          padding: EdgeInsets.only(top:height*0.06),
                          child: Center(
                            child: Text("Study Circle",
                            style: TextStyle(fontWeight: FontWeight.bold, fontSize: 50.0,),),
                          ),
                        ),
                        delay: delay+100,),
                        Padding(
                          padding:EdgeInsets.only(top:height*0.068,left: width*0.13),
                          child: Container(
                            height: height*0.34,
                            width: width*0.7,
                            child: Image.asset('assets/study.gif')),
                        )
                        ]),
                      delay: delay,
                      ),
            ShowUp(child: Text("Grow together, Learn together",
            style: TextStyle(fontFamily: 'Montserrat-ExtraBold',fontSize: 25.0),),
            delay: delay+100,),
            SizedBox(height:70.0),
          ShowUp(child: getButtonUI("Learn",selected=="Learn"),delay: delay+200),
          SizedBox(height:10.0),
          ShowUp(child: getButtonUI("Register Problem", selected=="Register Problem"),delay: delay+200,),
          SizedBox(height:10.0),
          ShowUp(child: getButtonUI("Provide Help", selected=="Provide Help"),delay: delay+200,),
                        ])
                        ),
      ]),
    )));
  }
   _getCurrentLocation() {
    geolocator.getCurrentPosition(desiredAccuracy: LocationAccuracy.best).then((Position position) {
      setState(() {
        _currentPosition = position;
      });
    }).catchError((e) {
      print(e);
    });
  }

  Widget getButtonUI(String select, bool isSelected) {
    String txt = select;
    var height=MediaQuery.of(context).size.height;
    var width=MediaQuery.of(context).size.width; 
    return Container(
      width: width*0.8,
      height: height*0.10,
      decoration: BoxDecoration(
          color: isSelected
              ? Colors.green
              : Colors.white,
          borderRadius: const BorderRadius.all(Radius.circular(24.0)),
          border: Border.all(color: Colors.green)),
          child: Padding(
            padding: const EdgeInsets.all(8.0),
            child: InkWell(
              splashColor: Colors.white24,
            borderRadius: const BorderRadius.all(Radius.circular(24.0)),
            onTap: (){
              setState(() {
                changeName(select);
                if(select=="Learn"){
                Navigator.push(context,MaterialPageRoute(
                  builder: (context) =>  start()));
                }else if(select=="Register Problem"){
                  Navigator.of(context).push(MaterialPageRoute(
                builder: (context) => AddProblem(lat:_currentPosition.latitude,long: _currentPosition.longitude)));
                }else{
                  Navigator.of(context).push(MaterialPageRoute(
                  builder: (context) => giveHelp()));
                }

              });
            }, 
            child: Center(
              child: Text(
                  txt,
                  style: TextStyle(
                    fontWeight: FontWeight.w600,
                    fontSize: 25,
                    letterSpacing: 0.27,
                    color: isSelected
                        ? Colors.white
                        : Colors.green,
                  ),
                ),
            ),
            ),
          ),
    );
  }
}