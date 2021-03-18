import 'package:flutter/material.dart';
import '../Utilities/ShowUp.dart';
import 'package:geolocator/geolocator.dart';
import 'homepage.dart';

// ignore: camel_case_types
class start extends StatefulWidget {
  @override
  _startState createState() => _startState();
}

// ignore: camel_case_types
class _startState extends State<start> {

  final Geolocator geolocator = Geolocator()..forceAndroidLocationManager;
  CategoryType categoryType = CategoryType.ds_algo;
  Position _currentPosition;
  String _currentAddress;
  var selectedCard;
  int delayAmount=500;

  void initState() {
    super.initState();
    _getCurrentLocation();
  }
  void changeName(CategoryType categoryTypeData){
    setState(() {
      categoryType = categoryTypeData;
      print(categoryType);
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.white,
      body: ListView(children: [
        Stack(children:[ 
          Padding(
            padding: EdgeInsets.only(top:MediaQuery.of(context).size.height*0.2),
            child: ShowUp(
                    child: Container(
                    height: MediaQuery.of(context).size.height*0.69,
                    width: MediaQuery.of(context).size.width,
                    color: Colors.transparent,
                    child: Padding(
            padding: EdgeInsets.only(
              top:MediaQuery.of(context).size.height*0.16,
              bottom:MediaQuery.of(context).size.height*0.46,
              left: MediaQuery.of(context).size.width*0.05,
              right: MediaQuery.of(context).size.width*0.05),
            child: ShowUp(
                            child: Container(
                            child:ListView(scrollDirection: Axis.horizontal,
                          children: <Widget>[
                            getButtonUI(CategoryType.ds_algo, categoryType == CategoryType.ds_algo),
                              const SizedBox(width: 16,),
                            getButtonUI(CategoryType.computer_networks, categoryType == CategoryType.computer_networks),
                              const SizedBox(width: 16,),
                            getButtonUI(CategoryType.operating_system, categoryType == CategoryType.operating_system),
                              const SizedBox(width: 16,),
                            getButtonUI(CategoryType.dbms, categoryType == CategoryType.dbms)  
                                  ],)    
                                ),
                            delay: delayAmount+400,
                        ),)),
                    delay: delayAmount+200,
              ),
          ),
          Padding(
            padding: EdgeInsets.only(bottom: MediaQuery.of(context).size.height*0.3),
            child: ShowUp(
                    child: Container(
                      decoration: BoxDecoration(
                        borderRadius: BorderRadius.only(
                          bottomLeft: Radius.circular(45.0),
                          bottomRight: Radius.circular(45.0),
                        ),
                          color: Color(0xFF7A9BEE)),
                      height: MediaQuery.of(context).size.height*0.33,
                      width: MediaQuery.of(context).size.width,
                      child: ListView(
                        shrinkWrap: true,
                        children: <Widget>[
                          Padding(
            padding: EdgeInsets.only(top:MediaQuery.of(context).size.height*0.02,left: MediaQuery.of(context).size.width*0.05),
            child: ShowUp(
                    child: Text(_currentAddress==null?"No Location Found":_currentAddress,
                    style: TextStyle(
                            fontFamily: 'Montserrat-ExtraBold',
                            fontSize: MediaQuery.of(context).size.width*0.03,)),
                            delay: delayAmount+200,
                    )),
                    Padding(padding: EdgeInsets.only(top:MediaQuery.of(context).size.height*0.05,left: MediaQuery.of(context).size.width*0.05),
        child:ShowUp(
                      child: Text("What would you like to read?",
                      style: TextStyle(
                              fontFamily: 'Montserrat-ExtraBold',
                              fontSize: MediaQuery.of(context).size.width*0.156,
                              fontWeight: FontWeight.bold)),
                          delay: delayAmount+200,
                      ),),
                      
                  ],),
                )
              )  
            ),
            Padding(
              padding: EdgeInsets.only(top:MediaQuery.of(context).size.height*0.47,
              left: MediaQuery.of(context).size.width*0.05,
              right: MediaQuery.of(context).size.width*0.05),
              child: Container(
                height: MediaQuery.of(context).size.height*0.48,
                child:(categoryType == CategoryType.ds_algo)?
                chaptersList("Algorithms","Data Structures","","","","","","",categoryType):(categoryType == CategoryType.computer_networks)?
                chaptersList("Data Link Layer","Network Layer","Transport Layer","Application Layer","","","","",categoryType):(categoryType == CategoryType.operating_system)?
                chaptersList("Process","Process Scheduling","Scheduling Algorithms","Virtual Memory","Other topics","","","",categoryType):(categoryType == CategoryType.dbms)?
                chaptersList("Introduction","ER Model","Relation Model","Relational Database","File Structure","Indexing & Hashing","","",categoryType):null
              ),
            ),                        
          ]
        )
      ],
    )
  );
}

  Widget chaptersList(String subject_1,String subject_2,String subject_3,String subject_4,String subject_5,String subject_6,String subject_7,String subject_8,CategoryType name)
  {
     return ShowUp(
                    child: Container(
                    child: ListView(
                    scrollDirection: Axis.vertical,
                    children: <Widget>[
                              subject_1.length>0?_buildInfoCard(subject_1,name):SizedBox(width: 0.0),
                              subject_2.length>0?_buildInfoCard(subject_2,name):SizedBox(width: 0.0),
                              subject_3.length>0?_buildInfoCard(subject_3,name):SizedBox(width: 0.0),
                              subject_4.length>0?_buildInfoCard(subject_4,name):SizedBox(width: 0.0),
                              subject_5.length>0?_buildInfoCard(subject_5,name):SizedBox(width: 0.0),
                              subject_6.length>0?_buildInfoCard(subject_6,name):SizedBox(width: 0.0),
                              subject_7.length>0?_buildInfoCard(subject_7,name):SizedBox(width: 0.0),
                              subject_8.length>0?_buildInfoCard(subject_8,name):SizedBox(width: 0.0)
                              ],
                    )
                ),
                  delay: delayAmount+400,
            );
  }

  Widget _buildInfoCard(String cardTitle,CategoryType sub) {
    // ignore: non_constant_identifier_names
    var subject=sub.toString().split(".")[1];
    var Imagename="assets/Subjects/"+subject+"/"+cardTitle+".jpg";
    return InkWell(
      onTap: () {
        selectCard(cardTitle);
        Navigator.pushReplacement(
        context,
        MaterialPageRoute(
          builder: (context) =>  MyHomePage(address: 'http://solutionchallenge.pythonanywhere.com/'+subject+'/'+cardTitle,category: cardTitle,subject:subject,lat: _currentPosition.latitude,long:_currentPosition.longitude),
        ),
      );
      },
      child: Stack(
              children:[ AnimatedContainer(
          duration: Duration(milliseconds: 500),
          curve: Curves.easeIn,
          decoration: BoxDecoration(
            borderRadius: BorderRadius.circular(50.0),
            //image: DecorationImage(
              //image: AssetImage(Imagename),
            //),
            border: Border.all(
              color: Colors.blue,
            width: MediaQuery.of(context).size.width*0.0009
            ),
          ),
          height: MediaQuery.of(context).size.height*0.324,
          width: MediaQuery.of(context).size.width*0.85,
          child: Column(
            mainAxisAlignment: MainAxisAlignment.spaceBetween,
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Padding(
                padding: EdgeInsets.only(top: 25.0,left: 40.0),
                child: Container(
                    child: FlatButton(child: Image(image: AssetImage(Imagename),),
                    onPressed: (){
                      Navigator.pushReplacement(
                      context,
                      MaterialPageRoute(
                      builder: (context) => MyHomePage(address: 'http://solutionchallenge.pythonanywhere.com/'+subject+'/'+cardTitle,category: cardTitle,subject:subject,lat: _currentPosition.latitude,long:_currentPosition.longitude),
                      ),
                    );
                    },),
                    width: MediaQuery.of(context).size.width*0.668,
                    height: MediaQuery.of(context).size.height*0.178,
                    decoration: new BoxDecoration(
                    color: Colors.blue,
                    shape: BoxShape.rectangle,
                    borderRadius: BorderRadius.circular(10.0),
                  ),
                ),
              ),
              Padding(
                padding: EdgeInsets.only(top: MediaQuery.of(context).size.width*0.001,left: MediaQuery.of(context).size.width*0.05,bottom: MediaQuery.of(context).size.height*0.04),
                child: Container(
                  width: MediaQuery.of(context).size.width*0.768,
                child: FlatButton(
                  child: Center(
                    child: Text(cardTitle,
                      style: TextStyle(
                        fontFamily: 'Montserrat-ExtraBold',
                        fontSize: MediaQuery.of(context).size.width*0.07,
                        fontWeight: FontWeight.bold,
                        color:Colors.white,
                      )),
                  ),
                  color: Colors.blue,
                  onPressed: (){
                  Navigator.pushReplacement(
                  context,
                  MaterialPageRoute(
                  builder: (context) => MyHomePage(address: 'http://solutionchallenge.pythonanywhere.com/'+subject+'/'+cardTitle,category: cardTitle,subject:subject,lat: _currentPosition.latitude,long:_currentPosition.longitude),
                  ),
                );
                },),
                decoration: new BoxDecoration(
                color: Colors.blue,
                shape: BoxShape.rectangle,
                borderRadius: BorderRadius.circular(10.0),
              ),
              )),
                  ],
                ),
              ),
              ])
      );
  }

  selectCard(cardTitle) {
    setState(() {
      selectedCard = cardTitle;
    });
  }
  _getCurrentLocation() {
    geolocator.getCurrentPosition(desiredAccuracy: LocationAccuracy.best).then((Position position) {
      setState(() {
        _currentPosition = position;
      });

      _getAddressFromLatLng();
    }).catchError((e) {
      print(e);
    });
  }

  _getAddressFromLatLng() async {
    try {
      List<Placemark> p = await geolocator.placemarkFromCoordinates(
          _currentPosition.latitude, _currentPosition.longitude);

      Placemark place = p[0];

      setState(() {
        _currentAddress =
            "${place.locality}, ${place.postalCode}, ${place.country}";
      });
    } catch (e) {
      print(e);
    }
  }
  Widget getButtonUI(CategoryType categoryTypeData, bool isSelected) {
    String txt = '';
    if (CategoryType.ds_algo == categoryTypeData) {
      txt = 'DS Algo';
    } else if (CategoryType.computer_networks == categoryTypeData) {
      txt = 'Computer Networks';
    } else if (CategoryType.operating_system == categoryTypeData) {
      txt = 'Operating System';
    } else if (CategoryType.dbms == categoryTypeData) {
      txt = 'DBMS';
    } 
    return Container(
      width: categoryTypeData.toString().length.toDouble()*5,
      decoration: BoxDecoration(
          color: isSelected
              ? Color.fromRGBO(0,0,205,1)
              : Colors.white,
          borderRadius: const BorderRadius.all(Radius.circular(24.0)),
          border: Border.all(color: Colors.blue)),
          child: Padding(
            padding: const EdgeInsets.all(8.0),
            child: InkWell(
              splashColor: Colors.white24,
            borderRadius: const BorderRadius.all(Radius.circular(24.0)),
            onTap: (){
              setState(() {
                changeName(categoryTypeData);
              });
            }, 
            child: Center(
              child: Text(
                  txt,
                  style: TextStyle(
                    fontWeight: FontWeight.w600,
                    fontSize: 12,
                    letterSpacing: 0.27,
                    color: isSelected
                        ? Colors.white
                        : Colors.blue,
                  ),
                ),
            ),
            ),
          ),
    );
  }
}

  enum CategoryType {
  ds_algo,
  computer_networks,
  operating_system,
  dbms,
}