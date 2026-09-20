## Kalkulačka nebezpečná

Nebezpečný vstup pro otevření terminálu na OS Linux s Gnome. Prví řádek vložte jako první číslo, druhý jako operátor a třetí jako druhé číslo:

```python
__import__('os').system('/bin/bash -c gnome-terminal') if 1
+
1 else 1
```

OS Mac:

```Python
__import__('os').system('open -a Terminal') if 1
+
1 else 1
```

[Referenční_řešení](calc_eval.py ":include :type=code python")

[Download](_examples/calc_eval.py ":ignore")
