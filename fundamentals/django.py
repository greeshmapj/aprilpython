#coding standards

results=[
    {"district":"tvm","win":98,"A+":45000},
    {"district":"ktm","win":95,"A+":40000},
    {"district":"apy","win":97,"A+":47000},
    {"district":"idk","win":90,"A+":38000},
    {"district":"ekm","win":99,"A+":56000},
    {"district":"pta","win":99,"A+":58000},
    {"district":"tsr","win":98,"A+":57000},
    {"district":"kzd","win":99,"A+":58000},
    {"district":"pd","win":95,"A+":50000},
    {"district":"mpm","win":90,"A+":4500}

]
#tvm_win=[result for result in results if result["district"]=="tvm"]
#print(tvm_win)

#results.sort(key=lambda res:res["win"],reverse=True)
#print(results)

print(sum([ res["A+"] for result in results]))
