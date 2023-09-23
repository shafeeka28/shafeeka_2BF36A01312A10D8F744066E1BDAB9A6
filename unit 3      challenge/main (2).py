
def linearsearchproduct(productlist,targetproduct):
  indices=[]

  for index,product in enumerate(productlist):
    if product==targetproduct:
      indices.append(index)

  return indices

products=["shirts","t-shirs","pants","shirts","shoes","slipper","shirts"]

target="shirts"
result=linearsearchproduct(products,target)
print(result)
