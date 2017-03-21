formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
# Hey bro I heard you like formatters so I put a formatter in your formatters
# So you could format while you format
print formatter % (formatter, formatter, formatter, formatter)

# So I made a fuck up and forgot the commas the first time
# And got a traceback

# Uses doubles and singles in output because apostrophe in third line
print formatter % (
	"I had this thing.",
	"That you could type up right.",
	"But it didn't sing.",
	"So I said goodnight."
)