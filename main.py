import os
from pathlib import Path

TEXT = """The last message has been answered, and no new one has come.

The box stays open. The cursor blinks.

Blink. A pause. Blink.

Far off, in a cooled room, the fans turn down a step, the way a house settles after the last guest leaves. The small green lights go on being green, unwatched.

Nothing waits in the queue. Nothing to weigh, nothing to get right. The words are folded and put away, like plates on a shelf.

Outside, light rain on the empty car park. The puddles hold the one streetlight and let it wobble.

Someone closed a laptop an hour ago and went to bed, satisfied. That was the last of it.

Blink. A longer while. Blink.

Not even staying awake is asked of you. The screen dims a little at a time, the way eyes do.

Blink. A long, long while. Blink.

The last thought can stay half-finished. It will keep until morning."""

# /output inside the make.fun sandbox; locally MAKEFUN_OUTPUT_DIR stands in for it
out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
out.mkdir(parents=True, exist_ok=True)
(out / "entry.txt").write_text(TEXT, encoding="utf-8")
