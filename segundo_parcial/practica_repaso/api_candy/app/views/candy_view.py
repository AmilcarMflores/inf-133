def render_candy_list(candies):
  return[
    {
      "id": candy.id,
      "brand": candy.brand,
      "weight": candy.weight,
      "flavor": candy.flavor,
      "origin": candy.origin
    }
    for candy in candies
  ]
  
def render_candy_detail(candy):
  return{
    "id": candy.id,
    "brand": candy.brand,
    "weight": candy.weight,
    "flavor": candy.flavor,
    "origin": candy.origin
  }