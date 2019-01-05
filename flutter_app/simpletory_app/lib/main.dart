// import 'dart:async';

import 'package:flutter/material.dart';
// import 'package:barcode_scan/barcode_scan.dart';
// import 'package:flutter/services.dart';

// import 'selectionScreen.dart';
import 'simpletory_list_item.dart';

void main() => runApp(MaterialApp(
      home: HomePage(),
      theme: ThemeData.dark(),
      routes:{
        '/listtest' : (context) => ListItemTestScreen(),
      }
    ));

// App Bar Class, currently just prints the name of the current app
class SimpletoryAppBar extends AppBar {
  SimpletoryAppBar({Key key, this.titleName})
      : super(title: Text("Simpletory: " + titleName));

  final titleName;
}

//Main screen, shows the primary icons
class HomePage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: SimpletoryAppBar(
        titleName: "Home Screen",
      ),
      body:  iconGrid,
    );
  }

  final Widget iconGrid = Center(
      child: Column(
          mainAxisAlignment: MainAxisAlignment.spaceAround,
          children: <Widget>[
        Row(mainAxisAlignment: MainAxisAlignment.spaceAround, children: [
          
          // Padding(padding: EdgeInsets.all(80), child: Text("")),
          _button("History","history", false,),
          _button("Pack", "pack", false),
        ]),
        Row(mainAxisAlignment: MainAxisAlignment.spaceAround, children: [
          _button("Add", "add", false),
          _button("List Pick", "list", false),
        ]),
        Row(mainAxisAlignment: MainAxisAlignment.spaceAround, children: [
          _button("Search", "search", false),
          _button("Pick", "qr", true),
        ]),
      ]));

  static _button(String buttonText, String buttonIndex, bool done,) {
    var possibleButtons = {
      "qr": Icon(Icons.center_focus_strong),
      "list": Icon(Icons.format_list_numbered),
      "search": Icon(Icons.search),
      "add": Icon(Icons.add_box),
      "pack": Icon(Icons.file_download),
      "history": Icon(Icons.history)
    };

    var buttonScreen ={
      "qr": Navigator.pushNamed(context, '/listtest'),
      // "qr" :(){},
      "list": (){},
      "search": (){},
      "add": (){},
      "pack": (){},
      "history": (){}
    };
// This is for development purposes, if it's red it's not implemented yet
    _isDone(done) {
      if (done) {
        return Colors.white;
      } else {
        return Colors.red;
      }
    }

    return Padding(
        padding: EdgeInsets.all(10),
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children:[IconButton(
          icon: possibleButtons[buttonIndex],
          iconSize: 120,
          onPressed: buttonScreen[buttonIndex],
          color: _isDone(done),
          tooltip: buttonText,
        ),
        Text(buttonText,
        style: TextStyle(fontSize: 20, fontWeight: FontWeight.bold )),
        ]
        ))
        ;
  }
}
