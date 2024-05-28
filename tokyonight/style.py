from pygments.style import Style
from pygments.token import Keyword, Name, Comment, String, Error, Literal, \
    Number, Operator, Other, Punctuation, Text, Generic, Whitespace

__all__ = ["TokyonightNightStyle"]

class TokyonightNightStyle(Style):
    name = "tokyonight-night"

    background_color = "#1a1b26"

    styles = {
        Whitespace: "bg:#1a1b26 #c0caf5",

        Comment: "italic #414868",
        Comment.Single: "italic #414868",
        Comment.Multiline: "italic #414868",
        Comment.Special: "italic #414868",
        Comment.Hashbang: "italic #414868",
        Comment.Preproc: "italic #414868",
        Comment.PreprocFile: "bold #414868",

        Generic: "#c0caf5",
        Generic.Inserted: "bg:#15161e #9ece6a",
        Generic.Deleted: "bg:#15161e #db4b4b",
        Generic.Emph: "italic",
        Generic.Strong: "bold",
        Generic.Underline: "underline",
        Generic.Heading: "bold #e0af68",
        Generic.Subheading: "bold #e0af68",
        Generic.Output: "#c0caf5",
        Generic.Prompt: "#c0caf5",
        Generic.Error: "#db4b4b",
        Generic.Traceback: "#db4b4b",

        Error: "#db4b4b",

        Keyword: "#bb9af7",
        Keyword.Pseudo: "#bb9af7",
        Keyword.Constant: "#e0af68",
        Keyword.Declaration: "#9d7cd8",
        Keyword.Namespace: "#7dcfff",
        Keyword.Type: "#41a6b5",

        Literal: "#c0caf5",
        Literal.Date: "#c0caf5",
        Literal.String: "#9ece6a",
        Literal.StringChar: "#9ece6a",
        Literal.StringSingle: "#9ece6a",
        Literal.StringDouble: "#9ece6a",
        Literal.StringBacktick: "#9ece6a",
        Literal.StringOther: "#9ece6a",
        Literal.StringSymbol: "#9ece6a",
        Literal.StringInterpol: "#9ece6a",
        Literal.StringAffix: "#9d7cd8",
        Literal.StringDelimiter: "#7aa2f7",
        Literal.StringEscape: "#7aa2f7",
        Literal.StringRegex: "#7dcfff",
        Literal.StringDoc: "#414868",
        Literal.StringHeredoc: "#414868",
        Literal.Number: "#e0af68",
        Literal.NumberBin: "#e0af68",
        Literal.NumberHex: "#e0af68",
        Literal.NumberInteger: "#e0af68",
        Literal.NumberFloat: "#e0af68",
        Literal.NumberIntegerLong: "#e0af68",
        Literal.NumberOct: "#e0af68",

        Name: "#c0caf5",
        Name.Class: "#ff9e64",
        Name.Constant: "#ff9e64",
        Name.Decorator: "bold #7aa2f7",
        Name.Entity: "#7dcfff",
        Name.Exception: "#e0af68",
        Name.Function: "#7aa2f7",
        Name.FunctionMagic: "#7aa2f7",
        Name.Label: "#9ece6a",
        Name.Namespace: "#e0af68",
        Name.Property: "#e0af68",
        Name.Tag: "#bb9af7",
        Name.Variable: "#c0caf5",
        Name.VariableClass: "#c0caf5",
        Name.VariableGlobal: "#c0caf5",
        Name.VariableInstance: "#c0caf5",
        Name.VariableMagic: "#c0caf5",
        Name.Attribute: "#7aa2f7",
        Name.Builtin: "#9ece6a",
        Name.BuiltinPseudo: "#9ece6a",
        Name.Other: "#c0caf5",

        Number: "#e0af68",

        Operator: "bold #9ece6a",
        Operator.Word: "bold #9ece6a",

        Other: "#c0caf5",

        Punctuation: "#c0caf5",

        String: "#9ece6a",

        Text: "#9ece6a", 
    }
