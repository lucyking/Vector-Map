# Vector-Map
Generate specific vector map with several parameters.


## Usage

```
python map.py -h
```
```
Usage: map.py [options]

Options:
  -h, --help            show this help message and exit
  -b N, --branch=N      set branch number<=N
  -n M, --node=M        set nodes number
  --min=Num             set min vector,min<=branch
  -x true, --xseq=true  gen breaking index list
  
```
## Example
```
python map.py -b 3 -n 5 --min 2
```
```
5
0,0,2,13
1,1,3,14
2,2,0,2
3,2,1,7
4,3,2,11
5,3,4,17
6,4,3,16
7,4,5,13
```

## Note
If you set min=N,in fact you may get N-1 vector,due to __one node has no vector to itself__.

## Todo
Add ```-d, --duplicate``` to option.   
At present now，you can trigger this fx in line:87 with comment.
