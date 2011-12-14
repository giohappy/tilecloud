<!doctype html>
<html>
	<head>
		<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
		<meta name="viewport" content="initial-scale=1.0, user-scalable=no">
%if debug:
		<link rel="stylesheet" href="/openlayers/theme/default/style.css" type="text/css">
		<script type="text/javascript" src="/openlayers/lib/OpenLayers.js"></script>
%else:
		<script type="text/javascript" src="/openlayers/build/OpenLayers.js"></script>
%end

		<style type="text/css">
			html, body, #map {
				margin: 0;
				padding: 0;
				height: 100%;
			}
		</style>
		<title>TileCloud</title>
	</head>
	<body>
		<div id="map" style="width: 100%; height: 100%;">
		</div>
		<script type="text/javascript">
			var map = new OpenLayers.Map({
				div: "map",
				allOverlays: true
			});
%for index, (name, tile_store) in enumerate(tile_stores):
%if tile_store.content_type is None or tile_store.content_type.startswith('image/'):
			map.addLayer(new OpenLayers.Layer.XYZ('{{name}}', '/data/image/{{index}}/tiles/${z}/${x}/${y}', {
				sphericalMercator: true
			}));
%end
%end
%if len(tile_stores) > 1:
			map.addControl(new OpenLayers.Control.LayerSwitcher());
%end
			map.addControl(new OpenLayers.Control.MousePosition());
			map.zoomToMaxExtent();
		</script>
	</body>
</html>
