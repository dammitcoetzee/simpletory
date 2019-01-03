library selectionScreen;

import 'dart:async';

import 'package:flutter/material.dart';
import 'package:barcode_scan/barcode_scan.dart';
import 'package:flutter/services.dart';

// Copyright 2017 The Chromium Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

// class selectionScreen extends StatefulWidget {
//   @override
//   selectionScreenState createState() {
//     return new selectionScreenState();
//   }
// }

class selectionScreen extends StatelessWidget {
  var result = 'text';
  Future _scanQR() async {
    try {
      String qrResult = await BarcodeScanner.scan();
      return qrResult;
    } on PlatformException catch (ex) {
      if (ex.code == BarcodeScanner.CameraAccessDenied) {

          return "Camera permission was denied";
        
      } else {

          return "Unknown Error $ex";

      }
    } on FormatException {
      
        return "You pressed the back button before scanning anything";

    } catch (ex) {
      
        return "Unknown Error $ex";

    }
  }

  Widget parentBox = Container(
      child:
          Column(mainAxisAlignment: MainAxisAlignment.spaceEvenly, children: [
    Image.network(
        'https://raw.githubusercontent.com/flutter/website/master/src/_includes/code/layout/lakes/images/lake.jpg',
        fit: BoxFit.fitWidth),
    Text("Parent"),
  ]));

  Widget childBox = Container(
      child:
          Column(mainAxisAlignment: MainAxisAlignment.spaceEvenly, children: [
    Image.network(
        'https://raw.githubusercontent.com/flutter/website/master/src/_includes/code/layout/lakes/images/lake.jpg',
        fit: BoxFit.fitWidth),
    Text("Child"),
  ]));

  Widget build(BuildContext context) {
    return Stack(children: <Widget>[
      Scaffold(
        appBar: AppBar(
          title: Text('Put in or Take Out'),
        ),
        body: Center(
            child: Container(
                margin: const EdgeInsets.symmetric(horizontal: 40),
                child: Column(
                  mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                  children: <Widget>[parentBox, childBox],
                ))),
      ),
      Positioned(
          bottom: 10,
          right: 10,
          child: Column(children: <Widget>[
            Padding(
                padding: EdgeInsets.all(10),
                child: FloatingActionButton.extended(
                  onPressed: _scanQR,
                  heroTag: null,
                  icon: Icon(Icons.photo_camera),
                  label: Text("Parent"),
                )),
            FloatingActionButton.extended(
              onPressed: () {},
              heroTag: null,
              icon: Icon(Icons.photo_camera),
              label: Text("Child"),
            )
          ])),
    ]);
  }
}
