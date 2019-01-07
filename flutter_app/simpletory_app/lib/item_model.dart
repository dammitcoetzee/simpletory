library item_model;

class Item{
  
  String itemName;
  int qty;

  Item(this.itemName, this.qty);

  itemUp(int incrementor){
    this.qty += incrementor;
  }
  
  itemDown(int decrementor){
    this.qty -= decrementor;
  }

}