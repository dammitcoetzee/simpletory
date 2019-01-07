library simpletory_list_item;
import 'package:flutter/material.dart';

import 'package:barcode_scan/barcode_scan.dart';
import 'package:flutter/services.dart';

import 'main.dart';

class ListItemTestScreen extends StatefulWidget{
  @override
  ListItemTestScreenState createState() => ListItemTestScreenState();
}

class ListItemTestScreenState extends State<ListItemTestScreen>{
  var _result = "Default String";
  @override
  Widget build(BuildContext context){
    return Scaffold(
      appBar: SimpletoryAppBar(context, titleName:"List Item Test"),
      body: Column(children: [RaisedButton(child:Text("Test Screen"), onPressed: _scanQR ,), Text(_result),RaisedButton(child:Text("ResetScan"), onPressed: () {setState(() {
              this._result = "RESET";
            });} ,)])
      );
  }
  Future _scanQR() async {
    try {
      String qrResult = await BarcodeScanner.scan();
      setState(() {
              this._result = qrResult;
            });
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
}

