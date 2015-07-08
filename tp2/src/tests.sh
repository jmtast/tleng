#!/bin/bash

TMP_FILE_OUT="file_out"
TMP_FILE_ERR="file_err"
RETURN_VAL=0

# Test de errores
for i in {1..12}; do
    ./musileng "../tests/test$i.in" $TMP_FILE_OUT 2> $TMP_FILE_ERR
    diff $TMP_FILE_ERR "../tests/test$i.out" > /dev/null
    if [ $? -ne 0 ]; then
        echo "Error en test $i"
        RETURN_VAL=1
    fi
done

exit $RETURN_VAL
