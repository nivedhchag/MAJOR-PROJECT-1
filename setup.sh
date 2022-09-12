mkdir -p ~/.streamlit/

echo"\
[server]\n\
headless = true\n\
port =$PORT\n\
enabeCORS = fasle\n\
\n\
" > ~/.streamlit/config.toml
