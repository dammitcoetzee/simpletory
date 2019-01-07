// import 'dart:async';

import 'package:flutter/material.dart';
// import 'package:barcode_scan/barcode_scan.dart';
// import 'package:flutter/services.dart';
// import 'package:flutter/cupertino.dart'; //uncomment to use cupertio icons
// import 'selectionScreen.dart';
import 'simpletory_list_item.dart';

void main() =>
    runApp(MaterialApp(home: HomePage(), theme: ThemeData.dark(), routes: {
      '/listtest': (BuildContext context) => ListItemTestScreen(),
      '/home':(BuildContext context) => HomePage()
    }));

// App Bar Class, currently just prints the name of the current app
class SimpletoryAppBar extends AppBar {
  SimpletoryAppBar(BuildContext context, {Key key, this.titleName})
      : super(title: Text("Simpletory: " + titleName),
      actions:<Widget>[
        IconButton(icon: Icon(Icons.home), onPressed: ()=> Navigator.pushNamed(context, '/home'),)
      ]);

  final titleName;
}

//Main screen, shows the primary icons
class HomePage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
        appBar: SimpletoryAppBar(context,
          titleName: "Home Screen",
        ),
        body: Center(
            child: Column(
                mainAxisAlignment: MainAxisAlignment.spaceAround,
                children: <Widget>[
              Row(mainAxisAlignment: MainAxisAlignment.spaceAround, children: [
                // Padding(padding: EdgeInsets.all(80), child: Text("")),
                _button(
                  "History",
                  "history",
                  false, context
                ),
                _button("Pack", "pack", false, context),
              ]),
              Row(mainAxisAlignment: MainAxisAlignment.spaceAround, children: [
                _button("Add", "add", false, context),
                _button("List Pick", "list", false, context),
              ]),
              Row(mainAxisAlignment: MainAxisAlignment.spaceAround, children: [
                _button("Search", "search", false, context),
                _button("Pick", "qr", true, context),
              ]),
            ])));
  }

   static _button(
    String buttonText,
    String buttonIndex,
    bool done,
    BuildContext context
  ) {
    final  possibleButtons = {
      // "qr": Icon(IconData(0xf3db, fontFamily: 'CupertinoIcons', fontPackage: 'cupertino_icons') ), //uncomment library above to use
      "qr": Icon(Icons.center_focus_strong), //android icon, might look better
      "list": Icon(Icons.format_list_numbered),
      "search": Icon(Icons.search),
      "add": Icon(Icons.add_box),
      "pack": Icon(Icons.file_download),
      "history": Icon(Icons.history)
    };

    final buttonScreen = {
      "qr": () => Navigator.pushNamed(context, '/listtest'),
      // "qr": () {},
      "list": () {},
      "search": () {},
      "add": () {},
      "pack": () {},
      "history": () {}
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
        child: Column(mainAxisAlignment: MainAxisAlignment.center, children: [
          IconButton(
            icon: possibleButtons[buttonIndex],
            iconSize: 120,
            onPressed: buttonScreen[buttonIndex],
            color: _isDone(done),
            tooltip: buttonText,
          ),
          Text(buttonText,
              style: TextStyle(fontSize: 20, fontWeight: FontWeight.bold)),
        ]));
  }
}
