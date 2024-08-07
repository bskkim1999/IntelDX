echo ">> first : "
read a
echo ">> second : "
read b
echo ">> a = $a, b = $b"

add=`expr $a + $b`
gob=`expr $a \* $b`
na=`expr $a / $b`
avg=`expr $add / 2`
echo "a+b=$add \na*b=$gob \na/b=$na \n(a+b)/2=$avg"

exit 0