//welcome_page.dart

import 'package:flutter/material.dart';
import 'package:flutter/widgets.dart';
import 'main.dart';

class WelcomePage extends StatelessWidget{
  @override

  Widget build(BuildContext context)
  {
    Color darkBlue = Color(0xFF001052);
    return Scaffold(
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.start,
          crossAxisAlignment: CrossAxisAlignment.center,
          children: [
            Padding(
              padding: const EdgeInsets.only(top: 50.0),
              child: Image.asset(
                'assets/images/alert_arrival.png',
                height: 300,
              ),//Adjust the top padding
            ),
            Padding(padding: const EdgeInsets.only(top: 100.0),
            child: Image.asset('assets/images/wifi.png',
            height: 200,
              color: darkBlue,
              ),
            ),
            const SizedBox(height: 30),
            Expanded(
              child: Padding(
                padding: const EdgeInsets.only(bottom: 80.0),
                child: Align(
                  alignment: Alignment.bottomCenter,
                  child: ElevatedButton(
                    onPressed: () {
                      Navigator.push(
                        context,
                        MaterialPageRoute(
                          builder: (context) => MyHomePage(
                            title: 'Alert Arrival',
                        ),
                      ),
                      );
                    },
              style: ButtonStyle(
                backgroundColor: MaterialStateProperty.all<Color>(darkBlue),
                padding: MaterialStateProperty.all<EdgeInsetsGeometry>(
                  const EdgeInsets.symmetric(horizontal: 70, vertical: 20),
                ),
                foregroundColor: MaterialStateProperty.all<Color>(Colors.white),
                elevation: MaterialStateProperty.all<double>(4.0),
              ),
              child: const Text(
                'Enter Application',
                style: TextStyle(
                  fontSize: 18,
                ),
              ),
            ),
                ),
            ),
            ),//add more design elements or widgets for welcome page
          ],
        ),
      ),
    );
  }
}