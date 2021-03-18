import 'package:flutter/material.dart';
import 'package:solution_challenge/Problem_Submission/Provide_Help.dart';
import 'detailsPage.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';
import '../Utilities/data.dart';
import '../Utilities/ShowUp.dart';
import 'package:marquee/marquee.dart';
import 'package:auto_size_text/auto_size_text.dart';
import 'package:fancy_drawer/fancy_drawer.dart';
import 'subHome.dart';
import 'package:solution_challenge/Problem_Submission/registerProblem.dart';

class MyHomePage extends StatefulWidget {
  final String category;
  final String address;
  final String subject;
  final double lat;
  final double long;
  MyHomePage({this.address,this.category,this.subject,this.lat,this.long});
  @override
  _MyHomePageState createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> with TickerProviderStateMixin{
  List<Posts> posts = List();
  List<Posts> ds = List();
  bool isLoaded = false;
  FancyDrawerController _controller;
  int delayAmount = 500;
  Future<void> _fetchData() async {
    try {
      print(widget.address);
      final response = await http.get(widget.address);
      if(response.statusCode==200){
        final data = json.decode(response.body);
        posts = (data['articles'] as List).map((data){  
          return Posts.fromJSON(data);
        }).toList();
        setState(() {
        this.isLoaded = true;
      });
      }
    }catch(e){
      print(e);
    }
  }
  
  void initState() {
    _fetchData();
    super.initState();
    _controller = FancyDrawerController(
      vsync: this, duration: Duration(milliseconds: 250))
    ..addListener(() {
      setState(() {}); // Must call setState
    });
  }
  @override
  void dispose() {
    _controller.dispose(); // Dispose controller
  super.dispose();
  }
  @override
  Widget build(BuildContext context) {
    final double width = MediaQuery.of(context).size.width;
    final double height = MediaQuery.of(context).size.height;
    return Material(
          child: FancyDrawerWrapper(
        backgroundColor: Colors.white, // Drawer background
	    controller: _controller,
        drawerItems: <Widget>[
          ListTile(
          title: Text('Home',style: TextStyle(
                              fontFamily: 'Montserrat',
                              color: Colors.black,
                              fontSize: width*0.063)),
          onTap: () {
            Navigator.of(context).pushReplacement(MaterialPageRoute(
                builder: (context) => start()));      
          }),
          widget.subject=='ds_algo'?drawing("Algorithms", widget.subject,widget.lat,widget.long):widget.subject=='computer_networks'?(drawing("Data Link Layer",widget.subject,widget.lat,widget.long)):
          widget.subject=='operating_system'?drawing("Process", widget.subject,widget.lat,widget.long):widget.subject=='dbms'?drawing("Introduction", widget.subject,widget.lat,widget.long):null,
          widget.subject=='ds_algo'?drawing("Data Structures", widget.subject,widget.lat,widget.long):widget.subject=='computer_networks'?(drawing("Network Layer", widget.subject,widget.lat,widget.long)):
          widget.subject=='operating_system'?drawing("Process Scheduling", widget.subject,widget.lat,widget.long):widget.subject=='dbms'?drawing("ER Model", widget.subject,widget.lat,widget.long):null,
          widget.subject=="computer_networks"?drawing("Transport Layer", widget.subject,widget.lat,widget.long):widget.subject=='operating_system'?drawing("Scheduling Algo", widget.subject,widget.lat,widget.long):
          widget.subject=='dbms'?drawing("Relation Model", widget.subject,widget.lat,widget.long):
          ListTile(
          title: Text('Register Problem',style: TextStyle(
                              fontFamily: 'Montserrat',
                              color: Colors.black,
                              fontSize: width*0.063)),
          onTap: () {
            Navigator.of(context).push(MaterialPageRoute(
                builder: (context) => AddProblem(lat: widget.lat,long: widget.long)));      
          },
        ),
          widget.subject=="computer_networks"?drawing("Application Layer", widget.subject,widget.lat,widget.long):widget.subject=='operating_system'?drawing("Virtual Memory", widget.subject,widget.lat,widget.long):
          widget.subject=='dbms'?drawing("Relational Database", widget.subject,widget.lat,widget.long):
          ListTile(
          title: Text('Provide Help',style: TextStyle(
                              fontFamily: 'Montserrat',
                              color: Colors.black,
                              fontSize: width*0.063)),
          onTap: () {
            Navigator.of(context).push(MaterialPageRoute(
                builder: (context) => giveHelp()));      
          },
        ),
        widget.subject=="computer_networks"?ListTile(
          title: Text('Register Problem',style: TextStyle(
                              fontFamily: 'Montserrat',
                              color: Colors.black,
                              fontSize: width*0.063)),
          onTap: () {
            Navigator.of(context).push(MaterialPageRoute(
                builder: (context) => AddProblem(lat: widget.lat,long: widget.long)));      
          }):widget.subject=='operating_system'?drawing("Process Scheduling", widget.subject,widget.lat,widget.long):widget.subject=='dbms'?drawing("File Structure", widget.subject,widget.lat,widget.long):null,
          widget.subject=="computer_networks"?ListTile(
          title: Text('Provide Help',style: TextStyle(
                              fontFamily: 'Montserrat',
                              color: Colors.black,
                              fontSize: width*0.063)),
          onTap: () {
            Navigator.of(context).push(MaterialPageRoute(
                builder: (context) => giveHelp()));      
          },
        ):widget.subject=='operating_system'?drawing("Process Scheduling", widget.subject,widget.lat,widget.long):widget.subject=='dbms'?drawing("Indexing & Hashing", widget.subject,widget.lat,widget.long):null,
        widget.subject=='operating_system'?ListTile(
          title: Text('Register Problem',style: TextStyle(
                              fontFamily: 'Montserrat',
                              color: Colors.black,
                              fontSize: width*0.063)),
          onTap: () {
            Navigator.of(context).push(MaterialPageRoute(
                builder: (context) => AddProblem(lat: widget.lat,long: widget.long)));      
          }):widget.subject=='dbms'?ListTile(
          title: Text('Register Problem',style: TextStyle(
                              fontFamily: 'Montserrat',
                              color: Colors.black,
                              fontSize: width*0.063)),
          onTap: () {
            Navigator.of(context).push(MaterialPageRoute(
                builder: (context) => AddProblem(lat: widget.lat,long: widget.long)));      
          }):null,
          widget.subject=='operating_system'?ListTile(
          title: Text('Provide Help',style: TextStyle(
                              fontFamily: 'Montserrat',
                              color: Colors.black,
                              fontSize: width*0.063)),
          onTap: () {
            Navigator.of(context).push(MaterialPageRoute(
                builder: (context) => giveHelp()));      
          },
        ):widget.subject=='dbms'?ListTile(
          title: Text('Provide Help',style: TextStyle(
                              fontFamily: 'Montserrat',
                              color: Colors.black,
                              fontSize: width*0.063)),
          onTap: () {
            Navigator.of(context).push(MaterialPageRoute(
                builder: (context) => giveHelp()));      
          },
        ):null
        ], 
          child: Scaffold(
            appBar: AppBar(elevation: 0.0,backgroundColor:Color(0xFF21BFBD),
            leading: IconButton(
                icon: Icon(
                  Icons.menu,
                  color: Colors.white,
                  size: height*0.043,
                ),
                onPressed: () {
                  _controller.toggle();
                },
              ),),
          backgroundColor: Color(0xFF21BFBD),
          body: ListView(
            children: <Widget>[
              Padding(
                padding: EdgeInsets.only(top: MediaQuery.of(context).size.height*0.0037, left: MediaQuery.of(context).size.width*0.49),
                child: Row(
                  mainAxisAlignment: MainAxisAlignment.spaceBetween,
                  children: <Widget>[
                  ],
                ),
              ),
              Padding(
                padding: EdgeInsets.only(left: MediaQuery.of(context).size.width*0.1017),
                child: Row(
                  children: <Widget>[
                    Padding(
                        padding: EdgeInsets.only(left:MediaQuery.of(context).size.width*0.337,),
                        child: ShowUp(
                          child: Text(
                            'Blogs',
                          style: TextStyle(
                            fontFamily: 'Montserrat',
                            color: Colors.white,
                            fontWeight: FontWeight.bold,
                            fontSize: width*0.059)),
                      delay: delayAmount,      
                        ),
                      ),
                    SizedBox(width: MediaQuery.of(context).size.width*0.0130),
                    Expanded(
                          child: Padding(
                        padding: const EdgeInsets.all(8.0),
                        child: ShowUp(
                              child: Text('For You',
                              style: TextStyle(
                                  fontFamily: 'Montserrat',
                                  color: Colors.white,
                                  fontSize: width*0.079)),
                         delay: delayAmount+200,         
                        ),
                      ),
                    ),      
                  ],
                ),
              ),
              SizedBox(height: MediaQuery.of(context).size.height*0.041),
              Row(
                children: [
                  widget.category=='Algorithms'?SizedBox(width: MediaQuery.of(context).size.width*0.502,):SizedBox(width: MediaQuery.of(context).size.width*0.421,),
                  Expanded(
                      child: ShowUp(
                          child: AutoSizeText(widget.category,
                          maxLines: 1,
                            style: TextStyle(
                                fontFamily: 'Montserrat',
                                color: Colors.white,
                                fontSize: width*0.076)),
                      delay: delayAmount+=100,         
                    ),
                  ),
                ],
              ),  
              SizedBox(height: MediaQuery.of(context).size.height*0.0124),
              ShowUp(
              child: Container(
              height: MediaQuery.of(context).size.height*0.781,
              decoration: BoxDecoration(
                color: Colors.white,
                borderRadius: BorderRadius.only(topRight: Radius.circular(75.0),topLeft: Radius.circular(75.0)),
              ),
              child: ListView(
                primary: false,
                padding: EdgeInsets.only(left: MediaQuery.of(context).size.width*0.0636, right: MediaQuery.of(context).size.width*0.050),
                children: <Widget>[
                  Padding(
                      padding: EdgeInsets.only(top: MediaQuery.of(context).size.height*0.055),
                      child: RefreshIndicator(
                      child:isLoaded?Container(
                          height: MediaQuery.of(context).size.height*0.625,
                          child: ListView.builder(
                            shrinkWrap:true,
                            itemCount:posts.length,
                            itemBuilder: (context,index)
                            {return ShowUp(
                                  child: _buildItem(posts[index].image,posts[index].title,posts[index].content,posts[index].text,
                              posts[index].video1,posts[index].video2,posts[index].video3,posts[index].video4),delay: delayAmount+60,
                            );})):Center(
                            child: CircularProgressIndicator()
                            ),onRefresh: _fetchData,)),
                ],
              ),
                  ),
                )
            ],
          ),
        ),
      ),
    );
  }
  Widget drawing(String sub,String subject,double lat,double long)
  {
    final double width = MediaQuery.of(context).size.width;
     return ListTile(
          title: Text(sub,style: TextStyle(
                              fontFamily: 'Montserrat',
                              color: Colors.black,
                              fontSize: width*0.063)),
          onTap: () {
            Navigator.of(context).pushReplacement(MaterialPageRoute(
                builder: (context) => MyHomePage(address:'http://solutionchallenge.pythonanywhere.com/'+subject+'/'+sub,category: sub,subject: subject,)));
          },
        );
  }
  Widget _buildItem(String imgPath, String name,String url,String text,String video1,String video2,String video3,String video4) {
    return Padding(
        padding: EdgeInsets.only(left: MediaQuery.of(context).size.width*0.01, right: MediaQuery.of(context).size.width*0.01, top: MediaQuery.of(context).size.height*0.01),
        child: InkWell(
          onTap: () {
            print(MediaQuery.of(context).size.height);
            print(MediaQuery.of(context).size.width);
            Navigator.of(context).push(MaterialPageRoute(
              builder: (context) => DetailsPage(img: imgPath, name: name,url: url,text: text,video1: video1,video2: video2,video3: video3,video4: video4)));
          },
          child: Row(
            mainAxisAlignment: MainAxisAlignment.spaceBetween,
            children: <Widget>[
              Container(
                child: Row(
                  children: [
                    Container(
                    decoration: BoxDecoration(
                      shape: BoxShape.circle,
                        image: DecorationImage(
                            image: NetworkImage(imgPath),
                            fit: BoxFit.cover)),
                    height: MediaQuery.of(context).size.height-733.0,
                    width: MediaQuery.of(context).size.width-312.0),
                    SizedBox(width: MediaQuery.of(context).size.width*0.025),
                    Container(
                            height: MediaQuery.of(context).size.height*0.0186,
                            constraints: BoxConstraints(maxWidth: MediaQuery.of(context).size.width * 0.42),
                            child: AutoSizeText(
                              name,
                              maxLines: 1,
                              overflowReplacement: Marquee(
                                text: name,
                                crossAxisAlignment: CrossAxisAlignment.start,
                                scrollAxis: Axis.horizontal,
                                blankSpace: 20.0,
                                velocity: 30.0,
                              ),
                            ),
                          ),
                  ]
                )
              ),
              IconButton(
                icon: Icon(Icons.arrow_forward_ios),
                color: Colors.black,
                onPressed: () {Navigator.of(context).push(MaterialPageRoute(
              builder: (context) => DetailsPage(img: imgPath, name: name,url: url,text: text,video1: video1,video2: video2,video3: video3,video4: video4)));}
              )
            ],
          )
        ));
  }
}
