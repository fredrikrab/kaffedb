rm -rf html
java -jar schemaspy-6.1.0.jar -t sqlite-xerial -db ../kaffe.db -u fredrik -o ./html -dp sqlite-jdbc-3.36.0.3.jar -cat coffee -s coffee -norows -imageformat png

FILE=/home/fredrik/erd.png
if [ -f "$FILE" ]; then
    convert -trim "$FILE" "../latex/images/er-diagram.png"
    rm $FILE
fi

convert "./html/diagrams/summary/relationships.real.large.png" -gravity South -chop 0x30 -trim "../latex/images/schemaspy.png"