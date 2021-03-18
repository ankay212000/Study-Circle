import 'dart:io';
import 'package:flutter/material.dart';
import 'package:image_picker/image_picker.dart';
import 'package:cloud_firestore/cloud_firestore.dart';
import 'package:firebase_core/firebase_core.dart'; 
import 'package:firebase_storage/firebase_storage.dart'; 
import 'package:solution_challenge/Utilities/ShowUp.dart';
import 'package:solution_challenge/Screens/subHome.dart';


class Take_image extends StatefulWidget {
  final String message;
  final double lat;
  final double long;
  Take_image({this.message,this.lat,this.long});
  @override
  _Take_imageState createState() => _Take_imageState();
}

class _Take_imageState extends State<Take_image> {
  PickedFile _imageFile;
  String _uploadedFileURL;
  var url="";
  final myController = TextEditingController();
  var delay=100;
  Future<void> captureImage(ImageSource imageSource) async {
    try {
      final imageFile = await ImagePicker().getImage(source: imageSource);
      setState(() {
        _imageFile = imageFile;
      });
    } catch (e) {
      print(e);
    }
  }
  Future uploadFile() async {    
   final Reference postImageRef =
          FirebaseStorage.instance.ref().child("");
      var timeKey = DateTime.now();
    
      print(_imageFile);
      UploadTask uploadTask = postImageRef.child(timeKey.toString() + ".jpg").putFile(File(_imageFile.path));
      _showToast(context, "Uploading, After Completion of Uploading automatic redirection to home....");
      _uploadedFileURL=await(await uploadTask).ref.getDownloadURL();
      setState(() {
        url=_uploadedFileURL.toString();
        print("Upload done");
        FirebaseFirestore.instance 
                      .collection('data') 
                    .add({'Problem': widget.message,'Connect via': myController.text.toString(),'Longitude':widget.long,'Latitude': widget.lat,'url':url});
        Navigator.pushReplacement(
                              context,
                          MaterialPageRoute(
                        builder: (context) =>start(),
        ),
        );
      });   
 }

  Widget _buildImage() {
    var height=MediaQuery.of(context).size.height;
    var width=MediaQuery.of(context).size.width;
    if (_imageFile != null) {
      return Container(
        height: height*0.15,
        width: width*0.8,
        child: Image.file(File(_imageFile.path)));
    } else {
      return Container(
        height: height*0.1,
        width: width*0.8,
        decoration: BoxDecoration(
          color: Colors.white,
          borderRadius: BorderRadius.only(
            bottomLeft:Radius.circular(45.0),
            bottomRight: Radius.circular(45.0),
            topLeft: Radius.circular(45.0),
            topRight: Radius.circular(45.0),
          )
        ), 
      child: Center(child: Text('No file chosen', style: TextStyle(fontSize: 18.0))));
    }
  }
  void _showToast(BuildContext context,String txt) {
  final scaffold = Scaffold.of(context);
  scaffold.showSnackBar(
    SnackBar(
      content: Text(txt),
      duration: Duration(seconds: 10000),
    ),
  );
}

  @override
  void initState() {
    super.initState();
    Firebase.initializeApp().whenComplete(() { 
      print("completed");
      setState(() {});
    });
  }
  @override
  Widget build(BuildContext context) {
    var width=MediaQuery.of(context).size.width;
    var height=MediaQuery.of(context).size.height;
    return ListView(
          scrollDirection: Axis.vertical,
          children: <Widget>[ Container(
        child: Stack(
          children: [
            ShowUp(
                child: Padding(
                padding: EdgeInsets.only(left:width*0.03),
                child: _buildImage(),
              ),
            delay: delay+100,),
            ShowUp(
                child: Padding(
                padding: EdgeInsets.only(top:height*0.2),
                child: _buildButtons(),
              ),
            delay: delay+300,
            ),
            ShowUp(
                child: Padding(
                padding: EdgeInsets.only(top:height*0.27),
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
                    hintText: "Phone number / email / instagram (to connect)",
                    hintStyle: TextStyle(
                        color: Colors.purple,
                        fontFamily: 'Montserrat-Italic',
                    )),
                    controller: myController,),
              ),
            delay: delay+500,),
            ShowUp(
                child: Padding(
                padding: EdgeInsets.only(top:height*0.35,left:width*0.32),
                child: FlatButton.icon(
                label: Text('Submit',style: TextStyle(color: Colors.blueAccent,fontSize: 20.0),),
                icon: Icon(Icons.cloud_upload,color: Colors.blueAccent,size: 25.0,),
                onPressed: (){ 
                  return showDialog( 
                context: context, 
                builder: (ctx) => AlertDialog( 
                  title: Text("Confirmation"), 
                  content: Text("Are you sure you want to Upload ?"), 
                  actions: <Widget>[ 
                    FlatButton( 
                      onPressed: () { 
                        Navigator.of(ctx).pop();
                        Navigator.pushReplacement(
                              context,
                          MaterialPageRoute(
                        builder: (context) =>start(),
                            ),
                        ); 
                      }, 
                      child: Text("Take me back to home"), 
                    ),
                    FlatButton( 
                      onPressed: () { 
                        Navigator.of(ctx).pop(); 
                      }, 
                      child: Text("No"), 
                    ), 
                    FlatButton( 
                      onPressed: () { 
                        print(myController.text.toString());
                        uploadFile();
                        print(url);
                    Navigator.of(ctx).pop(); 
                      }, 
                      child: Text("Yes Submit"), 
                    ), 
                  ], 
                ), 
              ); 
            }, 
                  )),
            delay: delay+700,)   
          ],
        ),
      ),
          ]);
  }

  Widget _buildButtons() {
    var height=MediaQuery.of(context).size.height;
    return ConstrainedBox(
        constraints: BoxConstraints.expand(height: height*0.06),
        child: Row(
            crossAxisAlignment: CrossAxisAlignment.stretch,
            mainAxisAlignment: MainAxisAlignment.spaceAround,
            children: <Widget>[
              getButtonUI(
                key: Key('retake'),
                txt: 'Gallery',
                onTap: () => captureImage(ImageSource.gallery),
              ),
              getButtonUI(
                key: Key('upload'),
                txt: 'Camera',
                onTap: () => captureImage(ImageSource.camera),
              ),
            ]));
  }

  Widget getButtonUI({Key key,String txt,Function onTap}) {
    return Container(
      width: MediaQuery.of(context).size.width*0.30,
      decoration: BoxDecoration(
          color: Colors.blueAccent,
          borderRadius: const BorderRadius.all(Radius.circular(24.0)),
          border: Border.all(color: Colors.blue)),
          child: Padding(
            padding: const EdgeInsets.all(8.0),
            child: InkWell(
              splashColor: Colors.white24,
            borderRadius: const BorderRadius.all(Radius.circular(24.0)),
            onTap: onTap, 
            child: Center(
              child: Text(
                  txt,
                  style: TextStyle(
                    fontWeight: FontWeight.w600,
                    fontSize: 20,
                    letterSpacing: 0.27,
                    color:Colors.white,
                  ),
                ),
            ),
            ),
          ),
    );
  }
}