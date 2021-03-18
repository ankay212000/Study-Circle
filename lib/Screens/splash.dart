import 'package:flutter/material.dart';
import 'package:lottie/lottie.dart';
import 'package:solution_challenge/Screens/afterSplash.dart';
import 'dart:async';


class SplashPage extends StatefulWidget {
  @override
  _SplashPageState createState() => _SplashPageState();
}

class _SplashPageState extends State<SplashPage> with TickerProviderStateMixin {
  AnimationController _controller;

  @override
  void initState() {
    super.initState();
    _controller =
        AnimationController(duration: const Duration(seconds: 6), vsync: this);
    playAnimation();
  }

  Future<void> playAnimation() async {
    try {
      await _controller.forward().orCancel;
    } on TickerCanceled {
      // the animation got canceled, probably because it was disposed of
    }

    Navigator.pushReplacement(
      context,
      MaterialPageRoute(
        builder: (context) =>  pageHome(),
        //MyHomePage(address: 'http://nitish21.pythonanywhere.com',category: 'Algorithms'),
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.black,
      body: StaggerAnimation(controller: _controller.view),
    );
  }
}

class StaggerAnimation extends StatelessWidget {
  StaggerAnimation({Key key, this.controller})
      : opacity = Tween<double>(
          begin: 0.0,
          end: 1.0,
        ).animate(
          CurvedAnimation(
            parent: controller,
            curve: Interval(
              0.0,
              0.300,
              curve: Curves.ease,
            ),
          ),
        ),
        width = Tween<double>(
          begin: 500.0,
          end: 200.0,
        ).animate(
          CurvedAnimation(
            parent: controller,
            curve: Interval(
              0.00,
              0.300,
              curve: Curves.ease,
            ),
          ),
        ),
        height = Tween<double>(
          begin: 500.0,
          end: 200.0,
        ).animate(
          CurvedAnimation(
            parent: controller,
            curve: Interval(
              0.00,
              0.300,
              curve: Curves.ease,
            ),
          ),
        ),
        color = ColorTween(
          begin: Colors.blue,
          end: Colors.lightBlueAccent,
        ).animate(
          CurvedAnimation(
            parent: controller,
            curve: Interval(
              0.300,
              0.600,
            ),
          ),
        ),
        textLength = Tween<double>(
          begin: 0,
          end: "Study Circle".length.toDouble(),
        ).animate(
          CurvedAnimation(
            parent: controller,
            curve: Interval(
              0.300,
              0.600,
              curve: Curves.ease,
            ),
          ),
        ),
        textLength2 = Tween<double>(
          begin: 0,
          end: "Circle".length.toDouble(),
        ).animate(
          CurvedAnimation(
            parent: controller,
            curve: Interval(
              0.600,
              0.900,
              curve: Curves.ease,
            ),
          ),
        ),
        sizedBoxHeight = Tween<double>(
          begin: 50,
          end: 0,
        ).animate(
          CurvedAnimation(
            parent: controller,
            curve: Interval(
              0.300,
              0.900,
              curve: Curves.ease,
            ),
          ),
        ),
        one = Tween<int>(
          begin: 0,
          end: 1,
        ).animate(
          CurvedAnimation(
            parent: controller,
            curve: Interval(
              0.300,
              0.300,
              curve: Curves.ease,
            ),
          ),
        ),
        two = Tween<int>(
          begin: 0,
          end: 1,
        ).animate(
          CurvedAnimation(
            parent: controller,
            curve: Interval(
              0.600,
              0.600,
              curve: Curves.ease,
            ),
          ),
        ),
        super(key: key);

  final Animation<double> controller;
  final Animation<double> opacity;
  final Animation<double> width;
  final Animation<double> height;
  final Animation<double> textLength;
  final Animation<double> textLength2;
  final Animation<double> sizedBoxHeight;
  final Animation<int> one;
  final Animation<int> two;
  final Animation<Color> color;

  static const TEXT_STYLE = TextStyle(
      fontSize: 35,
      fontWeight: FontWeight.w800,
      fontFamily: 'Montserrat',
      color: Colors.lightBlueAccent);
  //static const TEXT_STYLE2 = TextStyle(fontSize: 60.0, color: Colors.blueGrey);

  Widget _buildAnimation(BuildContext context, Widget child) {
    return Column(
      mainAxisAlignment: MainAxisAlignment.center,
      crossAxisAlignment: CrossAxisAlignment.center,
      children: <Widget>[
        SizedBox(
          height: sizedBoxHeight.value,
        ),
        Opacity(
          opacity: opacity.value,
          child: Container(
            height: MediaQuery.of(context).size.height*0.33,
            width: MediaQuery.of(context).size.height*0.4,
            child: Lottie.asset('assets/43885-laptop-working.json')
          ),
        ),
        SizedBox(
          height: 20.0,
        ),
        Row(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Text("Study Circle".substring(0, textLength.value.toInt()),
                style: TEXT_STYLE,),
          ],
        ),
      ],
    );
  }

  @override
  Widget build(BuildContext context) {
    return AnimatedBuilder(
      builder: _buildAnimation,
      animation: controller,
    );
  }
}

