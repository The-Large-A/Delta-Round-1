//stage 1 E-commerce Cart Management

var laptops = [
    { id: 1, name: 'Lenovo', ramSize: '8GB', storageSize: '256GB', price: 800 },
    { id: 2, name: 'Acer', ramSize: '16GB', storageSize: '512GB', price: 1200 },
    { id: 3, name: 'HP', ramSize: '32GB', storageSize: '1TB', price: 1800 }
  ];
  
  var cart = [];
  
  function addToCart(laptopId, RAMSize, storageSize) {
    var laptop = laptops.find(item => item.id === laptopId);
  
    if (!laptop) {
      console.log("Laptop not found.");
      return;
    }
  
    var cartItem = {
      laptopId: laptop.id,
      name: laptop.name,
      ramSize: RAMSize,
      storageSize: storageSize,
      price: laptop.price
    };
  
    cart.push(cartItem);
    console.log(`Added ${laptop.name} to the cart.`);
  }
  
  function removeFromCart(index) {
    if (index >= 0 && index < cart.length) {
      var removedItem = cart.splice(index, 1);
      console.log(`Removed ${removedItem[0].name} from the cart.`);
    } else {
      console.log("Invalid index.");
    }
  }
  
  function calculateTotal() {
    let total = 0;
    for (var item of cart) {
      total += item.price;
    }
    return total;
  }
  
  while (true) {
    console.log("\nOptions:");
    console.log("1. Add Laptop to Cart");
    console.log("2. Remove Item from Cart");
    console.log("3. View Cart");
    console.log("4. Calculate Total Price");
    console.log("5. Exit");
  
    var choice = prompt("Enter your choice (1/2/3/4/5):");
  
    switch (choice) {
      case '1':
        var laptopId = parseInt(prompt("Enter Laptop ID:"));
        var RAMSize = prompt("Enter RAM Size:");
        var storageSize = prompt("Enter Storage Size:");
        addToCart(laptopId, RAMSize, storageSize);
        break;
  
      case '2':
        var indexToRemove = parseInt(prompt("Enter the index of the item to remove:"));
        removeFromCart(indexToRemove);
        break;
  
      case '3':
        console.log("Cart Contents:");
        for (let i = 0; i < cart.length; i++) {
          var item = cart[i];
          console.log(`${i + 1}. ${item.name} - RAM: ${item.ramSize}, Storage: ${item.storageSize}, Price: $${item.price}`);
        }
        break;
  
      case '4':
        var total = calculateTotal();
        console.log(`Total Price: $${total}`);
        break;
  
      case '5':
        console.log("Exiting the program.");
        process.exit(0);
  
      default:
        console.log("Invalid choice. Please select a valid option.");
        break;
    }
  }
  