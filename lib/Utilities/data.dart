import 'package:json_annotation/json_annotation.dart';

@JsonSerializable(nullable: true)
class Posts {
  final String title;
  final String image;
  final String content;
  final String text;
  final String video1;
  final String video2;
  final String video3;
  final String video4;
  Posts({this.title,this.image,this.content,this.text,this.video1,this.video2,this.video3,this.video4});

  factory Posts.fromJSON(Map<String,dynamic> json) {
    return Posts(
      title: json['title'],
      image: json['image'],
      content: json['content'],
      text: json['text'],
      video1: json['Video_1'],
      video2: json['Video_2'],
      video3: json['Video_3'],
      video4: json['Video_4'],
    );
  }
}