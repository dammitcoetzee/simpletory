library simpletory_list_item;
import 'package:flutter/material.dart';

import 'main.dart';

class ListItemTestScreen extends StatelessWidget{
  @override
  Widget build(BuildContext context){
    return Scaffold(
      appBar: SimpletoryAppBar(titleName:"List Item Test"),
      body: Text("Test Screen")
      );
  }
}