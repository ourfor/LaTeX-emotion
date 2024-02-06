function unicodes(chs)
    local text = ""
    for _, c in utf8.codes(chs) do
        text = text .. unicode(c)
    end
    print(text)
end

function unicode(codepoint)
    local value = NULL
    if codepoint > 0xFFFF then
        value = string.format("^^^^^^%06x", codepoint)
    elseif codepoint > 0xFF then
        value = string.format("^^^^%04x", codepoint)
    else
        value = string.format("^^%02x", codepoint)
    end
    return value
end

unicodes("🀁♀")