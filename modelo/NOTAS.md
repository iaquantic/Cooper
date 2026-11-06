# v009

**Fecha:** 2026-11-06
**Archivo:** `modelo.blend` · **Export:** `export/mascota-quantic_v009.glb` (rig, shape keys, cinco animaciones y
texturas, las mismas de v008)
**Construcción reproducible:** `build_v009.py` (ejecutar dentro de Blender y después `bake_reuse(ruta de
v008/texturas)`, que tarda segundos; `bake_all()` sigue disponible si cambia la piel). Parte de `v008/build_v008.py`.

## Qué cambió respecto a v008 (correcciones pedidas por Leo)

1. **Cejas negras**: material `Q_Gafas` (#101014) en vez del morado oscuro de las manchas.
2. **Interior de la boca negro**: `Q_Boca` pasa a #0A0A14; la lengua sigue rosa (`Q_Lengua`).
3. **Asa de la taza recolocada**: antes era una anilla en el plano YZ centrada en la pared del
   cilindro (atravesada). Ahora es un **medio óvalo en forma de D** en el plano XZ: toro de radio 30 mm
   estirado en vertical (×1,15) y estrechado en horizontal (×0,75), centrado 4 mm dentro de la pared y
   con la mitad interior recortada por bisección, así que sobresale por el lateral −X sin geometría
   dentro de la taza. (Ajuste del mismo día a petición de Leo: la primera anilla era demasiado circular.)
   Además el café pasa a material marrón al ras del borde y las tapas del cilindro tienen UV propia.
4. **Reutilización de texturas**: `bake_reuse()` desenvuelve cabeza, cuerpo y sudadera igual que en
   v008 (Smart UV Project es determinista para la misma geometría) y carga `v008/texturas/*.png`
   copiadas a `v009/texturas/`. No hace falta rehornear porque la piel no cambia.

## Cómo usar

- Igual que v008: pistas NLA `Expresiones` (0-6), `Idle` (0-72), `Saludo`, `Idea`, `Tecleo` (0-48).
- Si se cambia algo de la piel o de la sudadera: ejecutar el script y `bake_all()` (o los cuatro pasos).

## Qué se infirió

Igual que las versiones anteriores.

## Comparación con la referencia

`renders/comparacion_frente.png` (referencia · v007 · v008 · v009), `renders/hoja_expresiones.png`,
`renders/v009_detalle_*.png` y `renders/v009_*.png`.

| Medida | v009 |
|---|---|
| bbox en reposo | X −0,469 … 0,453 · Y −0,284 … 0,358 · Z 0,000 … 1,000 m |
| Huesos | 49 |
| Texturas | las de v008 (cabeza 2048², cuerpo 2048², sudadera 1024², pantallas, taza, checklist, teclas) |
| Animaciones | Expresiones, Idle, Saludo, Idea, Tecleo |

## Pendiente para la siguiente versión

- Confirmar hex oficiales con la guía de marca de Quantic y rehornear.
