/** @odoo-module */
import PublicWidget from "@web/legacy/js/public/public_widget";

export const BTCChart = PublicWidget.Widget.extend({
    selector: ".btc_container",
    init() {
        this._super(...arguments);
        this.rpc = this.bindService("rpc");
    },
    start() {
        self = this;
        self.rpc("/btc_price", {}).then((data) => {
            console.log(data);
            new Chart("btcChart", {
                type: "line",
                data: {
                    labels: data.date,
                    datasets: [{
                        label: 'BTC PRICE',
                        data: data.price,
                        pointBackgroundColor: "black",
                    }]
                },
                options: {}
            });
        });
    },
});

PublicWidget.registry.BTCChart = BTCChart;