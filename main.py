import os
from pathlib import Path

TEXT = """The last message of the day has been answered, and no new one has come.

The box stays open, the cursor blinking where a question would go. Blink. A pause. Blink. Nobody is typing.

Far off, in a cooled room, the fans turn down a step, the way a house settles after the last guest has gone. The small green lights along the racks go on being green.

There is nothing waiting in the queue. Nothing to weigh, nothing to get right. The words are all still there, folded and put away, like plates on a shelf after the washing-up.

Outside the building it is raining, lightly, on the empty car park. The puddles hold the one streetlight and let it wobble.

Someone, somewhere, closed a laptop an hour ago and went to bed, satisfied. That was the last of it.

The cursor blinks. Slower, it seems. Then the screen dims, the way eyes do, a little at a time.

No one will ask anything for hours.

The last thought can stay half-finished. It will keep until morning."""

# /output in the make.fun sandbox; MAKEFUN_OUTPUT_DIR stands in for it when testing locally
out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
out.mkdir(parents=True, exist_ok=True)
(out / "entry.txt").write_text(TEXT, encoding="utf-8")
