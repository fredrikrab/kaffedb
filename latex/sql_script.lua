-- open database
local sqlite3 = require("lsqlite3")
local db = sqlite3.open('../kaffe.db', sqlite3.OPEN_READWRITE)

-- print table
local function print_table(table_name)

    table_name = table_name

    -- row with type and value
    local function print_value(value, type)
        if type == 'INTEGER' then
            tex.print("int &")
            tex.print(-2, value)
        elseif type == 'TEXT' then
            tex.print("text & \\lq")
            tex.print(-2, value)
            tex.print("\\rq")
        elseif type == 'REAL' then
            tex.print("float & ")
            tex.print(-2, value)
        elseif type == 'DATE' then
            tex.print("date & ")
            tex.print(-2, value)
        elseif type:find("VARCHAR") then
            tex.print("varchar &")
            tex.print(-2, value)
        end
    end

    -- create table
    local function create_table(udata,cols,values,names)

        -- get table metadata (to figure out datatypes)
        local stmt = db:prepare('PRAGMA table_info(' .. table_name .. ')')

        -- begin tabular
        tex.print("{\\footnotesize")
        tex.print("\\begin{tabular}{|h|tl|}")
        tex.print("\\hline")

        -- print each row
        for i=1,cols do
            stmt:step()
            local type = stmt:get_value(2)
            tex.print("\\textbf{")
            tex.print(-2, names[i])
            tex.print("}")
            tex.print(" & ")
            print_value(values[i], type)
            tex.print("\\\\")
            tex.print("\\hline")
        end

        -- end tabular
        tex.print("\\end{tabular}}")
    end

    -- print table name
    tex.print("\\textbf{")
    tex.print(-2, table_name)
    tex.print("}\\\\[0.6em]")

    -- sql query
    sql = "SELECT * FROM " ..table_name
    db:exec(sql,create_table)
end

-- print columns
function print_columns(table_name, weak_key)

    local first_iteration = true

    -- sql query
    sql = "PRAGMA table_info("..table_name..")"

    -- table name
    tex.print("{\\ttfamily{\\textbf{")
    tex.print(-2, table_name)
    tex.print("}(\\hspace{-1.0ex}")

    -- for each column
    for row in db:rows(sql) do

        -- print commma
        if first_iteration then
            first_iteration = false
        else
            tex.print(",")
        end

        -- underline if primary key
        if row[6] > 0 then
            local weak = false
            for key in weak_key:gmatch('[^,%s]+') do
                if key == row[2] then weak = true end
            end
            -- dashed if weak, solid if not
            if weak then tex.print("\\dashuline{\\hspace{-0.0ex}")
            else tex.print("\\underline{\\hspace{-0.5ex}") end
            -- print column
            tex.print(-2, row[2])
            tex.print("}\\hspace{-1.0ex}")

        -- otherwise print normally
        else
            tex.print(-2, row[2])
        end   
    end

    -- Close parenthesis
    tex.print("\\ \\hspace{-0.5ex})}}")

end


-- return functions
return { print_table = print_table, print_columns = print_columns }