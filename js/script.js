const configureFullPage = new fullpage('#fullpage', {

    // ──────────────────────────────────────────────────
	//   :::::: Barra de navegación
	// ──────────────────────────────────────────────────
    navigation: true, // Muesta la barra de navegación.
    menu: '#menu', // Menu de navegación.
    anchors: ['home', 'aboutUs', 'contactUs'], // Anclas, las usamos para identificar cada seccion y poder acceder a ellas con el menu.
    navigationTooltips: ['Home', 'About Us', 'Contact Us'], // Tooltips que mostrara por cada boton en el nav.
    showActiveTooltip: false, // Mostrar tooltip activa si estas en la seccion del tooltip.
});