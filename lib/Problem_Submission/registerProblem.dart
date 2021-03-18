import 'package:flutter/material.dart'; 
import 'package:lottie/lottie.dart';
import 'package:solution_challenge/Utilities/ShowUp.dart';
import 'Take_image.dart';

class AddProblem extends StatefulWidget  { 
  final String category;
  final String address;
  final String subject;
  final double lat;
  final double long;
  AddProblem({this.category,this.address,this.subject,this.lat,this.long});
  @override
  _AddProblemState createState() => _AddProblemState();
}

class _AddProblemState extends State<AddProblem> {
  var delay=100;
  final myController = TextEditingController();
  var section="Problem";
  @override
  void initState() {
    super.initState();
    }
    void dispose() {
    // Clean up the controller when the widget is removed from the widget tree.
    // This also removes the _printLatestValue listener.
    myController.dispose();
    super.dispose();
  }
  void changeName(String sec){
    setState(() {
      section= sec;
      print(section);
    });
  }
  @override
  Widget build(BuildContext context) {
    var height=MediaQuery.of(context).size.height;
    var width=MediaQuery.of(context).size.width;
    return Scaffold( 
      body:Stack(
        children:[
                Container(
                  child: ShowUp(
                    child: Lottie.asset('assets/43885-laptop-working.json'),
                    delay: delay,
                    ),
                ),
                Padding(
                  padding: EdgeInsets.only(top: height*0.43,left: width*0.03),
                  child: ShowUp(
                        child: Container(
                          height: MediaQuery.of(context).size.height*0.08,
                        child:ListView(scrollDirection: Axis.horizontal,
                        children: <Widget>[
                              getButtonUI("Problem", section=="Problem"),
                              SizedBox(width:30.0),
                              Icon(Icons.arrow_forward_ios),
                              SizedBox(width:30.0),
                              getButtonUI("Upload Photo", section=="Upload Photo"),
                                    ],)    
                                  ),
                              delay: delay+400,),
                ),
              Padding(
              padding: EdgeInsets.only(top:MediaQuery.of(context).size.height*0.53,
              left: MediaQuery.of(context).size.width*0.05,
              right: MediaQuery.of(context).size.width*0.05,
              bottom: height*0.01),
              child: Container(
                height: MediaQuery.of(context).size.height*0.48,
                decoration: BoxDecoration(
                        borderRadius: BorderRadius.only(
                          bottomLeft: Radius.circular(45.0),
                          bottomRight: Radius.circular(45.0),
                          topLeft: Radius.circular(45.0),
                          topRight: Radius.circular(45.0),
                        ),
                          color: Color(0xFF7A9BEE)),
                child:(section == "Problem")?
                writeProblem():uploadPhoto(myController)
              ),
            ),              
      ],  
    )); 
  }
  Widget writeProblem()
  {
    var width=MediaQuery.of(context).size.width;
    var delay=200;
     return ShowUp(
                    child: Container(
                    child: ListView(
                    scrollDirection: Axis.vertical,
                    children: <Widget>[
                              Padding(
                                padding: EdgeInsets.only(left:width*0.05,right:width*0.05),
                                child: Container(
                  child: TextField(
                    keyboardType: TextInputType.multiline,
                    maxLines: null,
                    decoration: InputDecoration(
                      filled: true,
                      fillColor: Colors.white,
                    enabledBorder: OutlineInputBorder(
                    borderRadius: BorderRadius.all(Radius.circular(10.0)),
                    borderSide: BorderSide(color: Colors.blueAccent),
                  ),
              focusedBorder: OutlineInputBorder(
              borderRadius: BorderRadius.all(Radius.circular(10.0)),
              borderSide: BorderSide(color: Colors.purple),
            ),
              hintText: "Write down we there to help you....",
              hintStyle: TextStyle(
                  color: Colors.purple,
                  fontFamily: 'Montserrat-Italic',
              ),
            ),
            controller: myController,
          ),
                ),
                              ),

                              ],
                    )
                ),
                  delay: delay+400,
            );
  }
  Widget uploadPhoto(TextEditingController mycontroller)
  {
    var height=MediaQuery.of(context).size.height;
    var width=MediaQuery.of(context).size.width;
    var delay=200;
     return ShowUp(
       child: Container(
         color: Colors.white,
         child: mycontroller.text.length==0?Padding(
           padding: EdgeInsets.only(top:height*0.11,left: width*0.01,right: width*0.01,bottom: height*0.2),
           child: Container(
             decoration: BoxDecoration(
               color: Colors.white,
               borderRadius: BorderRadius.only(
                            bottomLeft: Radius.circular(45.0),
                            bottomRight: Radius.circular(45.0),
                            topLeft: Radius.circular(45.0),
                            topRight: Radius.circular(45.0),
                          ),
             ),
             child: Center(child: Text("Before uploading Photo share your problem!!",style: TextStyle(color: Colors.red,fontSize: 18.0),)),),
         ):Take_image(message:mycontroller.text,lat: widget.lat,long: widget.long,)),
       delay: delay+400,
            );
  }
  Widget getButtonUI(String sec, bool isSelected) {
    String txt = '';
    if (sec == "Problem") {
      txt = 'Problem';
    } else if (sec=="Upload Photo") {
      txt = 'Upload Photo';
    }  
    return Container(
      width: MediaQuery.of(context).size.width*0.34,
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
                changeName(sec);
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

