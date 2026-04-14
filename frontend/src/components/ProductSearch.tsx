interface ProductSearchProps {
  value: string;
  onChange: (value: string) => void;
  onSearch: () => void;
  onClear: () => void;
}

export function ProductSearch({
  value,
  onChange,
  onSearch,
  onClear,
}: ProductSearchProps) {
  return (
    <div className="toolbar-card">
      <div className="toolbar-header">
        <div>
          <h2>Catálogo de produtos</h2>
          <p>Busque por id, nome ou categoria.</p>
        </div>
      </div>

      <div className="toolbar-row">
        <input
          value={value}
          onChange={(e) => onChange(e.target.value)}
          placeholder="Ex.: mouse, cadeira, informatica"
          className="input"
        />

        <button className="btn btn-primary" onClick={onSearch}>
          Buscar
        </button>

        <button className="btn btn-secondary" onClick={onClear}>
          Limpar
        </button>
      </div>
    </div>
  );
}