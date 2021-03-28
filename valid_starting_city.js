function validStartingCity(distances, fuel, mpg) {
  let left_fuel = 0;
  let min_fuel = 0;
  let min_idx = -1;
  for (let i = 0; i < distances.length; i++) {
    left_fuel += fuel[i] * mpg - distances[i];
    if (left_fuel < min_fuel) {
      min_fuel = left_fuel;
      min_idx = i;
    }
  }
  return (min_idx + 1) % fuel.length;
}
