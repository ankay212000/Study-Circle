import 'package:flutter/material.dart';
import '../Utilities/webview.dart';
import 'package:flutter/rendering.dart';
import 'package:url_launcher/url_launcher.dart';
import '../Utilities/ShowUp.dart';

class DetailsPage extends StatefulWidget {
  final img;
  final name;
  final url;
  final text;
  final String video1;
  final String video2;
  final String video3;
  final String video4;  
  DetailsPage({this.img, this.name,this.url,this.text,this.video1,this.video2,this.video3,this.video4});

  @override
  _DetailsPageState createState() => _DetailsPageState();
}

class _DetailsPageState extends State<DetailsPage> {

  var selectedCard;
  int delayAmount = 500;
  
  @override
  Widget build(BuildContext context) {
    final double width = MediaQuery.of(context).size.width;
    return Scaffold(
        backgroundColor: Color(0xFF7A9BEE),
        appBar: AppBar(
          leading: IconButton(
            onPressed: () {
              Navigator.of(context).pop();
            },
            icon: Icon(Icons.arrow_back_ios),
            color: Colors.white,
          ),
          backgroundColor: Colors.transparent,
          elevation: 0.0,
          title: Text('Here You Go!!',
              style: TextStyle(
                  fontFamily: 'Montserrat',
                  fontSize: width*0.045,
                  color: Colors.white)),
          centerTitle: true,
        ),
        body: ListView(children: [
          Stack(children: [
            ShowUp(
                  child: Container(
                  height: MediaQuery.of(context).size.height*0.89,
                  width: MediaQuery.of(context).size.width,
                  color: Colors.transparent),
                  delay: delayAmount+200,
            ),
            Padding(
              padding: EdgeInsets.only(top:MediaQuery.of(context).size.height*0.09),
              child: ShowUp(
                        child: Container(
                    decoration: BoxDecoration(
                        borderRadius: BorderRadius.only(
                          topLeft: Radius.circular(45.0),
                          topRight: Radius.circular(45.0),
                        ),
                        color: Colors.white),
                    height: MediaQuery.of(context).size.height*0.87,
                    width: MediaQuery.of(context).size.width,
                    child:Padding(
                      padding: EdgeInsets.only(top:MediaQuery.of(context).size.height*0.09,left: MediaQuery.of(context).size.width*0.06,right:MediaQuery.of(context).size.width*0.06),
                      child: ListView(
                        scrollDirection: Axis.vertical,
                  shrinkWrap: true,
                  children: <Widget>[
                      ShowUp(
                          child: Text(widget.name,
                            style: TextStyle(
                                fontFamily: 'Montserrat',
                                fontSize: width*0.056,
                                fontWeight: FontWeight.bold)),
                          delay: delayAmount+200,
                      ),
                      SizedBox(height: MediaQuery.of(context).size.height*0.024),
                      ShowUp(
                            child: Text(widget.text,
                            style: TextStyle(
                                fontFamily: 'Montserrat',
                                fontSize: width*0.050,
                                )),
                          delay: delayAmount+400,      
                      ),        
                      SizedBox(height: MediaQuery.of(context).size.height*0.024),
                      Row(
                        mainAxisAlignment: MainAxisAlignment.spaceBetween,
                        children: <Widget>[
                          ShowUp(
                                child: InkWell(
                                  onTap: (){
                                    Navigator.push(
                                              context,
                                      MaterialPageRoute(builder: (context) => WebView(widget.url, widget.name)));
                                  },
                              child: Container(
                              width: MediaQuery.of(context).size.width*0.32,
                              height: MediaQuery.of(context).size.height*0.049,
                              decoration: BoxDecoration(
                                    borderRadius: BorderRadius.circular(17.0),
                                    color: Color(0xFF7A9BEE)),
                              child: Row(
                                  mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                                  children: <Widget>[
                                    Text('View More',
                                    style: TextStyle(
                                        color: Colors.white,
                                        fontFamily: 'Montserrat',
                                        fontSize: width*0.0381))
                                  ],
                              ),
                            ),
                                ),
                          delay: delayAmount+400,  
                          )
                        ],
                      ),
                      SizedBox(height: MediaQuery.of(context).size.height*0.014),
                      SizedBox(height: MediaQuery.of(context).size.height*0.024),
                      ShowUp(
                            child: Text("Video Tutorials",
                            style: TextStyle(
                                fontFamily: 'Montserrat',
                                fontSize: width*0.056,
                                fontWeight: FontWeight.bold)),
                        delay: delayAmount+400,        
                      ),
                      SizedBox(height: MediaQuery.of(context).size.height*0.024),        
                      ShowUp(
                            child: Container(
                            height: MediaQuery.of(context).size.height*0.186,
                            child: ListView(
                              scrollDirection: Axis.horizontal,
                              children: <Widget>[
                                widget.video1!=null?_buildInfoCard('Video 1',widget.video1):SizedBox(width:0.0),
                                SizedBox(width: 10.0),
                                widget.video2!=null?_buildInfoCard('Video 2',widget.video2):SizedBox(width:0.0),
                                SizedBox(width: 10.0),
                                widget.video3!=null?_buildInfoCard('Video 3',widget.video3):SizedBox(width:0.0),
                                SizedBox(width: 10.0),
                                widget.video4!=null?_buildInfoCard('Video 4',widget.video4):SizedBox(width:0.0)
                              ],
                            )
                          ),
                          delay: delayAmount+400,
                      ),  
                  ],
                ),
                    ) ,),
              ),
            ),
            Padding(
              padding: EdgeInsets.only(top: MediaQuery.of(context).size.height*0.037,
                left: (MediaQuery.of(context).size.width / 2)*0.74,),
              child: Container(
                  decoration: BoxDecoration(
                    shape: BoxShape.circle,
                      image: DecorationImage(
                          image: NetworkImage(widget.img),
                          fit: BoxFit.cover)),
                  height: MediaQuery.of(context).size.height*0.13,
                  width: MediaQuery.of(context).size.width*0.25),
            ),
          ])
        ]));
  }

  Widget _buildInfoCard(String cardTitle,String add) {
    return InkWell(
      onTap: () {
        selectCard(cardTitle);
        _launchURL(add);
      },
      child: AnimatedContainer(
        duration: Duration(milliseconds: 500),
        curve: Curves.easeIn,
        decoration: BoxDecoration(
          borderRadius: BorderRadius.circular(10.0),
          color: cardTitle == selectedCard ? Color(0xFF7A9BEE) : Colors.white,
          border: Border.all(
            color: cardTitle == selectedCard ? 
            Colors.transparent :
            Colors.grey.withOpacity(0.3),
            style: BorderStyle.solid,
          width: MediaQuery.of(context).size.width*0.0019
          ),
          
        ),
        height: MediaQuery.of(context).size.height*0.124,
        width: MediaQuery.of(context).size.width*0.25,
        child: Column(
          mainAxisAlignment: MainAxisAlignment.spaceBetween,
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Padding(
              padding: EdgeInsets.only(top: MediaQuery.of(context).size.height*0.0062, left: MediaQuery.of(context).size.width*0.038),
              child: Text(cardTitle,
                  style: TextStyle(
                    fontFamily: 'Montserrat',
                    fontSize: MediaQuery.of(context).size.width*0.03,
                    color:
                        cardTitle == selectedCard ? Colors.white : Colors.black,
                  )),
            ),
            Padding(
              padding: EdgeInsets.only(left: MediaQuery.of(context).size.width*0.012, bottom: MediaQuery.of(context).size.height*0.043,right: MediaQuery.of(context).size.width*0.012),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: <Widget>[
                  Padding(
                    padding: EdgeInsets.only(bottom:MediaQuery.of(context).size.height*0.018,right: MediaQuery.of(context).size.width*0.127),
                    child: IconButton(
                      icon: Icon(Icons.play_arrow,size: 50.0,), 
                    onPressed:(){
                      //print("hi");
                      selectCard(cardTitle);
                      _launchURL(add);
                      }),
                  )
                ],
              ),
            )
          ]
        )
      )
    );
  }

  selectCard(cardTitle) {
    setState(() {
      selectedCard = cardTitle;
    });
  }
  _launchURL(String add) async {
  String url = add;
  if (await canLaunch(url)) {
    await launch(url);
  } else {
    throw 'Could not launch $url';
  }
}
}
