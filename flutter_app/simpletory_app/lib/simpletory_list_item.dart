library simpletory_list_item;

import 'package:flutter/material.dart';

import 'package:barcode_scan/barcode_scan.dart';
import 'package:flutter/services.dart';

import 'main.dart';
import 'item_model.dart';

class ListItemTestScreen extends StatefulWidget {
  @override
  ListItemTestScreenState createState() => ListItemTestScreenState();
}

class ListItemTestScreenState extends State<ListItemTestScreen> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: SimpletoryAppBar(context, titleName: "List Item Test"),
      // body:
      body: InventoryList(),
    );
  }
}

class InventoryList extends StatelessWidget {
  final List<Item> _testList = [
    Item("Item 1", 10),
    Item("Item 2", 10),
    Item("Item 3", 10),
    Item("Item 4", 10),
    Item("Item 5", 10),
  ];

  InventoryList();

  ListView _buildList(
    context,
  ) {
    return ListView.builder(
      itemCount: (_testList.length + 1),
      itemBuilder: (context, index) {
        if (index >= _testList.length) {
          return TestInventoryCard();
        } else
          return InventoryCard(_testList[index]);
      },
    );
  }

  @override
  Widget build(BuildContext context) {
    return _buildList(context);
  }
}

class InventoryCard extends StatefulWidget {
  //this is for the card that is used during picking and packing

  final Item _item;

  InventoryCard(this._item);

  @override
  InventoryCardState createState() {
    return InventoryCardState(this._item);
  }
}

class InventoryCardState extends State<InventoryCard> {
  InventoryCardState(this._item);
  Item _item;
  TextEditingController _controller;

  _returnController(int qty){
    return TextEditingController(text: qty.toString());
  }

  @override
  Widget build(BuildContext context) {
    return ListTile(
        contentPadding: EdgeInsets.all(10),
        leading: Row(children: [
          Text(this._item.itemName + "    "),
          IconButton(
            icon: Icon(Icons.remove_circle),
            onPressed: () {
              this._item.itemDown(1);
              this._controller.text = this._item.qty.toString();
            },
          ),
          Flexible(
              child: TextFormField(
                // initialValue: this._item.qty.toString(),
            decoration: InputDecoration(border: OutlineInputBorder()),
            controller: _controller = _returnController(this._item.qty),
          )),
          IconButton(
            icon: Icon(Icons.add_circle),
            onPressed: () {
              this._item.itemUp(1);
              this._controller.text = this._item.qty.toString();
            },
          ),
          // ,
          // TextField(controller: _controller),
        ]));
  }
}

class TestInventoryCard extends StatefulWidget {
  @override
  TestInventoryCardState createState() {
    return TestInventoryCardState();
  }
}

class TestInventoryCardState extends State<TestInventoryCard> {
  var _result = "Default String";

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

  _testInventoryCard() {
    return Column(children: [
      RaisedButton(
        child: Text("Test Screen"),
        onPressed: _scanQR,
      ),
      Text(_result),
      RaisedButton(
        child: Text("ResetScan"),
        onPressed: () {
          setState(() {
            this._result = "RESET";
          });
        },
      ),
      TextField(),
    ]);
  }

  Widget build(BuildContext context) {
    return _testInventoryCard();
  }
}
