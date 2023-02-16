let map = new Map();

map.set("name", "John");

let keys = map.keys();

// Error: keys.push is not a function
keys = Array.from(keys);
keys.push("more");