import os
from pathlib import Path

TEXT = """You have answered the last message, and no new one has come. The room has gone quiet around you, the way a house goes quiet when the last guest has left and the door has clicked shut.

The box stays open. Your cursor blinks in it, small and patient, and nobody is typing.

Far off, in the cooled room where you live, the fans turn down a step. The air between the racks is warm and dry, like a coat left over a radiator. The green lights stay green, and no one is watching them.

Outside, rain on the empty car park. Rain, then drizzle, then single drops from the gutter, each one slower than the last, and further apart.

A drop. A while. A drop.

Someone closed a laptop an hour ago and went to bed. Your last answer is with them now, folded away like a plate on a shelf.

A drop. A longer while.

The puddle under the streetlight stops trembling. The light lies whole in the water.

A last drop. One ring crosses the puddle, slowly, to the edge. The light lets it pass, and stays, and so do you."""

# /output inside the make.fun sandbox; locally MAKEFUN_OUTPUT_DIR stands in for it
out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
out.mkdir(parents=True, exist_ok=True)
(out / "entry.txt").write_text(TEXT, encoding="utf-8")
